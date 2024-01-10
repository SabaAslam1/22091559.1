# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:41:35 2024

@author: DELL
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec

# Assuming df is your DataFrame with 'Country', 'DLRate', and 'populationpercentage' columns
df = pd.read_excel('Computer_Literacy.xlsx')
df = df.dropna(subset=['DLRate'])
df_sorted = df.sort_values(by='DLRate', ascending=False)
totalpopulation = df['Population (est)'].sum()
df_sorted['DLRate'] = (df['DLRate'] * 100).round(2)
df_sorted['populationpercentage'] = (df_sorted['Population (est)'] / totalpopulation) * 100

# Top five bar plot
top_five = df_sorted.head(5)
melted_df_top = pd.melt(top_five, id_vars=['Country'], value_vars=['populationpercentage', 'DLRate'],
                        var_name='Variable', value_name='Value')
melted_df_top['Value'] = pd.to_numeric(melted_df_top['Value'], errors='coerce')

# Bottom five bar plot
bottom_five = df_sorted.tail(5)
melted_df_bottom = pd.melt(bottom_five, id_vars=['Country'], value_vars=['populationpercentage', 'DLRate'],
                           var_name='Variable', value_name='Value')
melted_df_bottom['Value'] = pd.to_numeric(melted_df_bottom['Value'], errors='coerce')

# Pie chart for top five mobile users
total_android_users_top = top_five['Android Users'].sum()
total_ios_users_top = top_five['iOS Users'].sum()
labels_top_pie = ['Android Users', 'iOS Users']
sizes_top_pie = [total_android_users_top, total_ios_users_top]

# Pie chart for bottom five mobile users
total_android_users_bottom = bottom_five['Android Users'].sum()
total_ios_users_bottom = bottom_five['iOS Users'].sum()
labels_bottom_pie = ['Android Users', 'iOS Users']
sizes_bottom_pie = [total_android_users_bottom, total_ios_users_bottom]

# Pie chart for top five mobile users
totalpopulation_top = top_five['Population (est)'].sum()
mobilephone_top = top_five['Smart Phone Users'].sum()
percentagemobileUser_top = (mobilephone_top / totalpopulation_top) * 100
nonmobileuser_top = 100 - percentagemobileUser_top

# Pie chart for bottom five mobile users
totalpopulation_bottom = bottom_five['Population (est)'].sum()
mobilephone_bottom = bottom_five['Smart Phone Users'].sum()
percentagemobileUser_bottom = (mobilephone_bottom / totalpopulation_bottom) * 100
nonmobileuser_bottom = 100 - percentagemobileUser_bottom

# Create a dashboard with gridspec
fig = plt.figure(figsize=(20, 15))
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])

# Add title at the top
fig.suptitle('Digital Literacy Rate', fontsize=24, fontweight='bold', color='darkblue')

# Add name and student ID on either side with increased size
fig.text(0.01, 0.95, 'Name: Saba Aslam', ha='left', va='center', fontsize=18, fontweight='bold')
fig.text(0.99, 0.95, 'Student ID: 22091559', ha='right', va='center', fontsize=18, fontweight='bold')

# Top five bar plot
ax0 = plt.subplot(gs[0])
barplot_top = sns.barplot(x='Country', y='Value', hue='Variable', data=melted_df_top,
                          palette={'DLRate': 'orange', 'populationpercentage': 'skyblue'}, ax=ax0)
ax0.set_title('Countries with Highest Digital Literacy Rate', fontsize=16, fontweight='bold', color='green')

# Bottom five bar plot
ax1 = plt.subplot(gs[1])
barplot_bottom = sns.barplot(x='Country', y='Value', hue='Variable', data=melted_df_bottom,
                             palette={'DLRate': 'orange', 'populationpercentage': 'skyblue'}, ax=ax1)
ax1.set_title('Countries with Lowest Digital Literacy Rate', fontsize=16, fontweight='bold', color='red')

# Top five pie chart
ax2 = plt.subplot(gs[2])
ax2.pie(sizes_top_pie, labels=labels_top_pie, autopct='%1.1f%%', startangle=140)
ax2.set_title('Mobile Distribution - Top Five', fontsize=16, fontweight='bold', color='purple')

# Bottom five pie chart
ax3 = plt.subplot(gs[3])
ax3.pie(sizes_bottom_pie, labels=labels_bottom_pie, autopct='%1.1f%%', startangle=140)
ax3.set_title('Mobile Distribution - Bottom Five', fontsize=16, fontweight='bold', color='orange')

# Add summary at the end
summary_text = '''
Summary: Digital literacy attains its zenith in countries with relatively low global population shares, 
a trend notably exemplified by the Faroe Islands, boasting a 100% literacy rate yet accounting for a 
mere 0.001% of the world's populace. Among the top five countries with the highest digital literacy rates, 
China stands out, holding 26.15% of the world's population. Remarkably, the nations leading in digital literacy 
are characterized by markedly lower overall population sizes. Conversely, Indonesia, with a digital literacy rate 
of 3.4%, represents a larger segment of the global population at 5.20%. Striking parallels emerge in mobile technology 
usage, with 88.6% and 80.5% of Android users in countries with the lowest and highest digital literacy respectively. 
56% people only use mobile phones in highly literate countries, and 94.2% of people use mobile phones in the lowest 
digital literacy countries.
'''

fig.text(0.5, 0.02, summary_text, ha='center', va='center', fontsize=14, color='darkblue', bbox=dict(boxstyle="round", ec=(0.5, 0.5, 0.5), fc=(0.9, 0.9, 0.9)))


# Show the dashboard
plt.show()
