# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW6
# Question 1

import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# PART 1: READ DATASET ----------------------------
pd.set_option('display.max_columns', None)
df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
                 '/hw6_files/titanicTrain.csv')
# PART 2: DATA EXPLORATION AND FIND TARGET VARIABLE. COMMENTED OUT TO SAVE OUTPUTS
# TARGET VARIABLE: 'SURVIVED'

# sb.pairplot(df)
# plt.show()
# print(df)

# PART 3: DROP FACTORS THAT ARE NOT RELEVANT FOR LOGISTIC REGRESSION
dfClean = df[['Sex', 'Age', 'Pclass', 'Survived']]

# PART 4: MAKE SURE NO NULL / FILL NULL
# this is how we find what is null in the dataframe so we can drop it
# print(df.isnull().any())
# print(df.isnull().sum())
dfClean['Age'] = dfClean['Age'].fillna(dfClean['Age'].mean())

# PART 5: PLOT ONTO A COUNT GRAPH WITH ALL THE FACTORS
sb.countplot(data=dfClean)
plt.show()

# PART 6: CREATING DUMMY VARIABLES FOR CATEGORICAL DATA ----------------------
dfSex = pd.get_dummies(dfClean['Sex'])
dfClean = pd.concat([dfClean, dfSex], axis=1)
dfPclass = pd.get_dummies(dfClean['Pclass'])
dfClean = pd.concat([dfClean, dfPclass], axis=1)

# PART 7: PARTITION DATA INTO TRAINING SET ------------------------------------
# print(dfClean)
X = dfClean.loc[:, ['Age', 'female', 'male', 1, 2, 3]]
y = dfClean['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2020, test_size=0.3)

# PART 8: FIT THE DATA
# print(X.shape)
# print(y.shape)

# instantiate the model using default param
logReg = LogisticRegression()
# fit the model with the data
logReg.fit(X_train, y_train)
# make predictions
y_predict = logReg.predict(X_test)

# PART 9/10 : ACCURACY AND CONFUSION MATRIX
cnf_matrix = metrics.confusion_matrix(y_test, y_predict)
# print(cnf_matrix)
print('\n\nACCURACY SCORE: ', metrics.accuracy_score(y_test, y_predict))
metrics.plot_confusion_matrix(logReg, X_test, y_test)
plt.xticks(ticks=[0, 1], labels=['no', 'yes'])
plt.yticks(ticks=[0, 1], labels=['no', 'yes'])
plt.show()

# PART 11: PREDICTING MALE ADULT PASSANGER IN 3RD CLASS
passenger = [[30,0,1, 0,0,1]]
if not logReg.predict(passenger):
    print('THE TEST CASE DID NOT SURVIVE (NO)')
else:
    print('THE TEST CASE SURVIVED(YES')
