# Shantanu Jhaveri
# ITP 449 Fall 2020
# Final Project
# Q4

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import Ridge
from yellowbrick.regressor import ResidualsPlot

df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
                 '/finalproject_files/project_data/auto-mpg.csv')

# PART A
print('DATA FRAME SUMMARY:')
print(df.describe())
print('\nTHE MEAN MPG', df['mpg'].mean())

# PART B
print('THE MEDIAN MPG', df['mpg'].median())

# PART C
print('THE MEAN IS HIGHER THAN THE MEDIAN')
# PLOT

# PART D
plt.figure(1)
df_clean = df.drop(['No'], axis=1)
sns.pairplot(df_clean)
plt.show()

# PART E
print('THE STRONGEST CORRELATION IS BETWEEN MPG AND DISPLACEMENT')

# PART F
print('THE WEAKEST CORRELATION IS BETWEEN WEIGHT AND ACCELERATION')

# PART G
plt.figure(2)
plt.scatter(df_clean['displacement'], df_clean['mpg'])
plt.xlabel('Displacement')
plt.ylabel('mpg')
plt.show()

# PART H
plt.figure(3)
model = LinearRegression(fit_intercept=True)
X_train, X_test, y_train, y_test = train_test_split(df_clean.displacement, df_clean.mpg)
LR = LinearRegression()
LR.fit(X_train.values.reshape(-1, 1), y_train.values)
prediction = LR.predict(X_test.values.reshape(-1, 1))
plt.plot(X_test, prediction, label="Linear Regression", color='b')
plt.scatter(X_test, y_test, label="Actual Testing Data", color='g')
plt.legend()
plt.show()
print('INTERCEPT : ', LR.intercept_)
print('COEFFICIENT : ', LR.coef_)
print('EQUATION : [y = ', LR.intercept_, ' + ', LR.coef_, 'x]')
print('PREDICTED MPG FOR DISPLACEMENT 220 : ', LR.predict(np.array([[220]]))[0])
x = df_clean['displacement'].values
# RESHAPING JUST INCASE THE ARRAY IS NOT A 2D ARRAY
X = x.reshape(-1, 1)
y = df_clean['mpg']
ridge = Ridge()
visualizer = ResidualsPlot(ridge)
visualizer.fit(X, y)
visualizer.show()
