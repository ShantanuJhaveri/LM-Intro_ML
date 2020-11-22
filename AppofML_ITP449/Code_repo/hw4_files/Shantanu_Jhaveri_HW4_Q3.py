# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW4
# Question 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_US = pd.read_csv('/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw4_files/06-14-2020.csv')
df_US = df_US.set_index('Province_State')

df_US_highestActive = df_US.nlargest(2, "Active")
# QUESTION 1: NEW YORK IS THE HIGHEST ACTIVE STATE

# QUESTION 2: CONNECTICUT HAS THE HIGHEST MORTALITY RATE / FATALITY RATE
df_US_mortality = df_US[['Mortality_Rate']].copy()
df_US_mortality = df_US.nlargest(2, 'Mortality_Rate')

# QUESTION 3: THE DIFFERENCE IS 17880.53697 BTW THE MOST AND THE LEAST
df_US_test = df_US[['Testing_Rate']].copy()
df_US_test = df_US_test.dropna()
df_US_test = df_US_test.sort_values(by='Testing_Rate', ascending=False)
dif_maxmin_test = df_US_test.loc["Rhode Island"] - df_US_test.loc["Puerto Rico"]
# print(dif_maxmin_test)

# QUESTION 4/5: DEATH AND CONFIRMED CASE GRAPHS
pd.set_option('display.max_columns', None)
df_confirmed = pd.read_csv('/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw4_files'
                           '/time_series_covid19_confirmed_US(1).csv')
df_death = pd.read_csv('/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw4_files'
                       '/time_series_covid19_deaths_US(1).csv')
df_confirmed = df_confirmed.set_index('Province_State')
df_death = df_death.set_index('Province_State')
# Confirmed
df_US_confirmed = df_US['Confirmed'].copy().sort_values(ascending=False)
df_confirmed = df_confirmed.drop(
    columns={'UID', 'iso2', 'iso3', 'code3', 'Admin2', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'FIPS'})
df_confirmed = df_confirmed.groupby(['Province_State']).sum()
df_confirmed = df_confirmed.T
df_confirmed = df_confirmed[{'New York', 'New Jersey', 'California', 'Illinois', 'Massachusetts'}]
# Death
df_death = df_death.drop(
    columns={'UID', 'iso2', 'iso3', 'code3', 'Admin2', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'FIPS',
             'Population'})
df_death = df_death.groupby(['Province_State']).sum()
df_death = df_death.T
df_death = df_death[{'New York', 'New Jersey', 'California', 'Illinois', 'Massachusetts'}]

# plotting

# fig, axes = plt.subplots(1, 2, figsize=(...))
# df_confirmed.plot(ax=axes[0])
# axes[0].set_title(...)
# df_deaths.plot(ax=axes[1])
# axes[1].set_title(...)
# plt.show()

myFig = plt.figure()
confirmed = myFig.add_subplot(1, 2, 1)
plt.plot(df_confirmed)
plt.legend({'New York', 'New Jersey', 'California', 'Illinois', 'Massachusetts'})
plt.title('Confirmed Cases in the top 5 States')
plt.xlabel('Time')
plt.ylabel('Number of People')

death = myFig.add_subplot(1, 2, 2)
plt.title('Death in the top 5 States')
plt.legend({'New York', 'New Jersey', 'California', 'Illinois', 'Massachusetts'})
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.xticks(
    # ("3/1/2020", "5/1/2020", "7/1/2020", "9/1/2020","")
           )
plt.plot(df_death)

plt.show()

print(df_confirmed)
