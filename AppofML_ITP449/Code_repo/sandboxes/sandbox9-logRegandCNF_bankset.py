import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
bank_df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                      '/Code_repo/sandboxes/sandbox-data/banking.csv', header=0)
# print(bank_df.head())
# print(bank_df.shape)
# print(bank_df.columns.values)

# print(bank_df.isnull().sum())
# no null

# plt.figure(1)
# sb.countplot(x='y',data=bank_df)
# plt.figure(2)
# sb.countplot(x='job',data=bank_df)
# plt.figure(3)
# sb.countplot(x="marital",data=bank_df)
# plt.show()

bank_df = bank_df[['job', 'marital', 'default', 'housing', 'loan', 'poutcome', 'y']]
bank_df2 = pd.get_dummies(bank_df, columns=['job', 'marital', 'default', 'housing', 'loan', 'poutcome'])
# drop the rows with "unknown" values
bank_df2.drop(bank_df2.columns[[12, 16, 18, 21, 24]], axis=1, inplace=True)
# print(bank_df2.columns.values)
y = bank_df2.iloc[:, 0]
X = bank_df2.iloc[:, 1:]
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.linear_model import LogisticRegression
logReg = LogisticRegression()
logReg.fit(X_train,y_train)
y_predict = logReg.predict(X_test)

from sklearn import metrics

print('Accuracy:',metrics.accuracy_score(y_test,y_predict))
cnf_matrix = metrics.confusion_matrix(y_test,y_predict)
print(cnf_matrix)

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(logReg, X_test, y_test)
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_predict))

