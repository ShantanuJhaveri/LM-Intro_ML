import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
                 '/sandboxes/sandbox-data/titanicTrain.csv')

# print(df.head())
# print(df.info())
# print(df.describe())
# this is how we find what is null in the dataframe so we can drop it
# print(df.isnull().any())
# print(df.isnull().sum())

# drop all rows that have missing values (samples)
# dfDropRows = df.dropna(axis=0)
# print(dfDropRows.info())

# drop all columns with missing values (features)
# dfDropColumns = df.dropna(axis=1)
# print(dfDropColumns.info())

dfClean = df.dropna(subset=['Embarked'])
dfClean = dfClean.drop(columns=['Cabin'])
# print(dfClean.info())
dfClean['Age'] = dfClean['Age'].fillna(dfClean["Age"].mean())
dfSex = pd.get_dummies(dfClean['Sex'])
dfClean = pd.concat([dfClean, dfSex], axis=1)
# print(dfClean.head())

from sklearn.model_selection import train_test_split

y = dfClean['Survived']
X = dfClean.loc[:, ['Pclass', 'Age', 'female', 'male']]

X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.3)
