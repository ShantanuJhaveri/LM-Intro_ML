# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW5
# Question 1

import matplotlib.pyplot as plt
import pandas as pd


# Part 1: Preparation
df_avocado = pd.read_csv('/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw5_files/avocado.csv')
df_avocado = df_avocado[['Date', 'AveragePrice', 'Total Volume']].copy()
df_avocado['Date'] = pd.to_datetime(df_avocado['Date'])
df_avocado = df_avocado.sort_values(by='Date',ascending=True)
print(df_avocado)

# Part 2: Plotting
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.plot(df_avocado['Date'],df_avocado['AveragePrice'],'o',markersize=0.2)
ax1.set_xticks([])
ax1.set_xlabel(xlabel='Time', fontsize=7)
ax1.set_ylabel(ylabel='Average Price', fontsize=7)
ax2 = fig.add_subplot(2,2,2)
ax2.set_xticks([])
ax2.plot(df_avocado['Date'],df_avocado['Total Volume'],'o',markersize=0.2)
ax2.set_xlabel(xlabel='Time', fontsize=7)
ax2.set_ylabel(ylabel='Average Volume', fontsize=7)

df_avocado1 = df_avocado.copy()
df_avocado1['TotalRevenue'] = df_avocado1['Total Volume'] * df_avocado1['AveragePrice']
df_avocado1 = df_avocado1.groupby('Date').sum()
df_avocado1['AveragePrice'] = df_avocado1['TotalRevenue']/df_avocado1['Total Volume']

# Print the DataFrame that was just constructed
print(df_avocado1)
x = ["2015-01", "2015-05", "2015-09", "2016-01", "2016-05", "2016-09",
     "2017-01", "2017-05", "2017-09", "2018-01", "2018-05"]

# Print the individual smoothed curves
ax3 = fig.add_subplot(2,2,3)
ax3.plot(df_avocado1['AveragePrice'], marker='o', markersize=2)
ax3.set_xlabel(xlabel='Time', fontsize=7)
ax3.set_ylabel(ylabel='Average Price', fontsize=7)
ax3.set_xticklabels(x, rotation='vertical')
ax4 = fig.add_subplot(2,2,4)
ax4.plot(df_avocado1['Total Volume'], marker='o',markersize=2)
ax4.set_xlabel(xlabel='Time', fontsize=7)
ax4.set_ylabel(ylabel='Total Volume', fontsize=7)
ax4.set_xticklabels(x, rotation='vertical')
#
plt.show()

# Part 3: Plotting
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.plot(df_avocado1['AveragePrice'].rolling(20).mean(), marker='o',markersize=2)
ax1.set_xlabel(xlabel='Time', fontsize=7)
ax1.set_ylabel(ylabel='Average Price', fontsize=7)
ax1.set_xticklabels(x, rotation='vertical')
ax2 = fig.add_subplot(2,2,2)
ax2.plot(df_avocado1['AveragePrice'].rolling(20).mean(), marker='o',markersize=2)
ax2.set_xlabel(xlabel='Time', fontsize=7)
ax2.set_ylabel(ylabel='Total Volume', fontsize=7)
ax2.set_xticklabels(x, rotation='vertical')
#
plt.show()