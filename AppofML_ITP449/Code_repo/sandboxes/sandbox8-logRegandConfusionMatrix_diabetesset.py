import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pd.set_option('display.max_columns', None)
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
                   '/sandboxes/sandbox-data/diabetes.csv', header=1, names=col_names)

feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols]  # features
y = pima.label  # target variable

# print(X.head())
# print(y.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model using default param
logReg = LogisticRegression()
# fit the model with the data
logReg.fit(X_train, y_train)
# make predictions
y_predict = logReg.predict(X_test)

# eval performance
from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_predict)
print(cnf_matrix)
print('Accuracy = ', metrics.accuracy_score(y_test, y_predict))

