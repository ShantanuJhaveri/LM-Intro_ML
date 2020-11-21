# Shantanu Jhaveri
# ITP 449 Fall 2020
# Final Project
# Q2

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix

pd.set_option('display.max_columns', None)
bank_df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                      '/Code_repo/finalproject_files/project_data/UniversalBank.csv')

bank_df = bank_df.drop(['Row', 'ZIP Code'], axis=1)
ploan_df = bank_df['Personal Loan']
bank_df = bank_df.drop(['Personal Loan'], axis=1)
# print(bank_df)
# print(bank_df.info())
# TARGET VARIABLE = Personal Loan
X = bank_df
y = ploan_df

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020, stratify=y)

numofAcceptors = y_train.sum()
print('NUMBER OF ACCEPTORS IN THE TRAINING DATA: ', numofAcceptors)

dt = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=2020)
dt.fit(X_train, y_train)
y_predict = dt.predict(X_test)
plt.figure(1, figsize=(13, 10))
fn = X.columns
cn = y.unique()
irisTree = tree.plot_tree(dt, fontsize=12, filled=True, feature_names=fn, class_names=['Accepted', 'Rejected'])
plt.show()

# print(accuracy_score(y_train))

plt.figure(2)
plot_confusion_matrix(dt, X_train, y_train)
plt.show()

print('ON THE TRAINING DATA, 32 ACCEPTORS WERE CLASSIFIED AS NON-ACCEPTORS')
print('ON THE TRAINING DATA, 12 NON-ACCEPTORS WERE CLASSIFIED AS ACCEPTORS')
print('ACCURACY ON THE TRAIN PARTITION', accuracy_score(y_test, y_train))
print('ACCURACY ON THE TEST PARTITION', accuracy_score(y_test, y_predict))
