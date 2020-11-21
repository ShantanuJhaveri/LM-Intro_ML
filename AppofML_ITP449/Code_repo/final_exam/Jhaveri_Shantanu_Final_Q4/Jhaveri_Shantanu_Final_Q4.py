# Shantanu Jhaveri
# ITP 449 Fall 2020
# FINAL
# Question 3

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix

# PT 1
pd.set_option('display.max_columns', None)
ccDefaults_df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                            '/Code_repo/final_exam/Jhaveri_Shantanu_Final_Q4/ccDefaults(1).csv')

# PT 2
# print(ccDefaults_df.isnull().sum())
# print(ccDefaults_df.info())
print('\nTHERE ARE 25 NON-NULL FEATURES, AND 0 NULL SAMPLES\n')

# PT 3
print('DF HEAD\n',ccDefaults_df.head())

# PT 4
print('\nDIMENSION OF DF:', ccDefaults_df.shape)

# PT 5
ccDefaults_df = ccDefaults_df.drop(['ID'], axis=1)

# PT 6
ccDefaults_df.drop_duplicates(keep='first', inplace=True)

# PT 7
print('CORRELATION MATRIX\n',ccDefaults_df.corr())

# PT 8
X = ccDefaults_df[['PAY_1','PAY_2','PAY_3','PAY_4']]
y = ccDefaults_df['dpnm']

# PT 9
scaler = StandardScaler()
scaler.fit(X)
X = pd.DataFrame(scaler.transform(X), columns=X.columns)

# PT 10
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=2020, stratify=y)

# PT 11
dt = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=2020)
dt.fit(X_train, y_train)
y_predict = dt.predict(X_test)
y_predictTrain = dt.predict(X_train)

# PT 12
print('\nACCURACY ON THE TRAIN PARTITION', accuracy_score(y_train, y_predictTrain))
print('ACCURACY ON THE TEST PARTITION', accuracy_score(y_test, y_predict))

# PT 13
plt.figure(1)
plot_confusion_matrix(dt, X_test, y_test)
plt.show()

# PT 14
plt.figure(2, figsize=(13, 10))
fn = X.columns
cn = list(map(str, dt.classes_.tolist()))
irisTree = tree.plot_tree(dt, fontsize=12, filled=True, feature_names=fn, class_names=cn)
plt.show()
