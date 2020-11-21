# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW3
# Question 2

# Plot the global temperature for the past 140 years.
# a. Choose Time Scale - Annual
# b. Enable Options –Display Trend and per decade
# c. Then download as csv file
# d. Edit the csv file to keep only the Year and Value data, delete any header text in the csv
# file.
# e. Use pandas to read this csv file.

import pandas as pd
import matplotlib.pyplot as plt

global_df = pd.read_csv("/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw3_files/data.csv")
# print(global_df['Value'])
# x = [global_df['Year']]
# y = [global_df['Value']]
plt.plot(global_df['Year'], global_df['Value'], markersize=4, marker='o', color='r', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.title('Global Temperature')
plt.suptitle('Jhaveri_Shantanu_HW3_Q2')
plt.show()