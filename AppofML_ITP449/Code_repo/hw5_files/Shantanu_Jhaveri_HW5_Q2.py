# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW5
# Question 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import residuals_plot as rp

# Part 1: Stat Summary + Histogram + Pre-processing
df_CSL = pd.read_csv(
    '/Users/shantanujhaveri/Desktop/Class_Archives/AppofML_ITP449/workspace/hw5_files/CommuteStLouis.csv')
print(df_CSL[{'Age', 'Distance', 'Time'}].describe())
plt.hist(df_CSL['Age'])
plt.xlabel('Age')
plt.ylabel('Freq')
plt.title('Histogram of Age')
plt.show()

# Part 2: Correlation Matrix
print(df_CSL[{'Age', 'Distance', 'Time'}].corr())
sns.pairplot(df_CSL[{'Age', 'Distance', 'Time'}])
plt.show()
sns.boxplot(x="Sex", y="Distance", data=df_CSL, order=["M", "F"])
plt.show()

# Part 3: scatter plot with Linear regression
sns.lmplot(x="Distance", y="Time", data=df_CSL).set(title="Scatter plot and Linear Regression of Time vs Distance")
plt.show()

# Part 4: Distribution of residuals of the data
model = LinearRegression()
x = df_CSL['Distance'].values
X = x.reshape(-1, 1)
# X = X[:, np.newaxis]
y = df_CSL['Time']
# y.reshape(-1, 1)
model.fit(X, y)

viz = rp(model, y_train=y, X_train=X)
viz.fit(X, y)
viz.show()
