# Shantanu Jhaveri
# ITP 449 Fall 2020
# Final Project
# Q3

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', None)
df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
                 '/finalproject_files/project_data/mushrooms.csv')

# print(df.info())
# print(df.isnull().sum())\

X = df.drop(['class'], axis=1)
y = df['class']
X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=2020, stratify=y)

dt = DecisionTreeClassifier(max_depth=6, random_state=2020)
dt.fit(X_train, y_train)
y_predict = dt.predict(X_test)
y_predictTrain = dt.predict(X_train)

# PART A
plt.figure(1)
plot_confusion_matrix(dt, X_test, y_test)  # Testing Data
plt.figure(2)
plot_confusion_matrix(dt, X_train, y_train)  # Training Data
plt.show()

# PART B/C
print('\nACCURACY ON THE TRAIN PARTITION', accuracy_score(y_train, y_predictTrain))
print('ACCURACY ON THE TEST PARTITION', accuracy_score(y_test, y_predict))

# PART D
plt.figure(2, figsize=(20, 10))
fn = X.columns
cn = list(map(str, dt.classes_.tolist()))
irisTree = tree.plot_tree(dt, fontsize=12, filled=True, feature_names=fn, class_names=cn)
plt.show()

# PART E
pd.set_option('display.max_rows', None)
index_feature = 0
index_column = 0
# for i in dt.feature_importances_:
#     print(index_feature, ' : ', i)
#     index_feature += 1
# for i in X.columns:
#     print(index_column, ' : ', i)
#     index_column += 1

print('Feature Importance:', dt.feature_importances_)
print('MOST IMPORTANT FEATURES: ODOR, STALK ROOT, STALK SURFACE ABOVE RING')
# PART F
print('PREDICTION FOR TEST CASE : ', dt.predict(
    ['X', 'S', 'N', 'T', 'Y', 'G', 'C', 'N', 'K', 'E', 'E', 'S', 'S', 'W', 'W', 'P', 'W', 'O', 'P', 'R', 'S', 'U']))
