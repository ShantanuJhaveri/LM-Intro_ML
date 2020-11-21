# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW8
# Question 1

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

# PART 1: IMPORT DATAFRAME AND ACCOUNT FOR DISPLAY
pd.set_option('display.max_columns', None)
diabetes_knn = pd.read_csv(
    '/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
    '/hw8_files/diabetes.csv')
# PART 2: PRINT DIMENSIONS OF DATAFRAME
print('DIMENSIONS OF DATARFAME: ', diabetes_knn.shape)

# PART 3: LOOKING FOR NULL OR MISSING DATA. FOUND NOTHING THAT NEEDS TO BE REPLACED.
# COMMENTED OUT THIS SECTION SO I DO NOT HAVE TO WORRY ABOUT THE PRINT STATEMENTS
# print(diabetes_knn.info())
# print(diabetes_knn.head())
# print(diabetes_knn.isnull().any())
# dfDropRows = diabetes_knn.dropna(axis=0)
# print(dfDropRows.info())
# dfDropColumns = diabetes_knn.dropna(axis=1)
# print(dfDropColumns.info())
# print(diabetes_knn.shape)
# print(dfDropRows.shape)
# print(dfDropColumns.shape)
print(diabetes_knn.head())

# PART 4: CREATE FEATURE MATRIX (X) AND TARGET VECTOR(y)
X = diabetes_knn.iloc[:, 0:8]
y = diabetes_knn.iloc[:, 8]

# PART 5: STANDARDIZE
scaler = StandardScaler()
scaler.fit(X)
X = pd.DataFrame(scaler.transform(X), columns=X.columns)

# PART 6: SPIT THE DATA INTO SETS
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020, stratify=y)

# PART 7: DEVELOP KNN AND GET ACCURACY
neighbors = np.arange(1, 16)
trainAccuracy = np.empty(15)
testAccuracy = np.empty(15)

for k in neighbors:
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(X_train, y_train)
    y_predict = kNN.predict(X_test)
    trainAccuracy[k - 1] = kNN.score(X_train, y_train)
    testAccuracy[k - 1] = kNN.score(X_test, y_test)
    print('K= ', k, '; ACCURACY = ', accuracy_score(y_test, y_predict))

# PART 8: PLOT ACCURACY SCORING
plt.figure(1)
plt.plot(neighbors, testAccuracy, label='Testing Accuracy', marker='o')
plt.plot(neighbors, trainAccuracy, label='Training Accuracy', marker='o')
plt.xticks(neighbors)
plt.title('kNN: Varying Number of Neighbors')
plt.xlabel('k = Number of Neighbors')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# PART 9: BEST K + CNF_MATRIX
kNN = KNeighborsClassifier(n_neighbors=5)
kNN.fit(X_train, y_train)
y_predict = kNN.predict(X_test)
print('\n\nK=5 IS BEST. TRAINING ACCURACY: ', kNN.score(X_train, y_train), ' TESTING ACCURACY: ',
      kNN.score(X_test, y_test))
print('\nPRINTED CONFUSION MATRIX:\n', confusion_matrix(y_test, y_predict))
plt.figure(2)
plot_confusion_matrix(kNN, X_test, y_test)
plt.show()

# PART 10: PREDICT
testCase = [[2, 150, 85, 22, 200, 30, 0.3, 55]]
if kNN.predict(testCase):
    print('OUTCOME OF TEST CASE PATIENT: ', kNN.predict(testCase), '(YES)')
else:
    print('OUTCOME OF TEST CASE PATIENT: ', kNN.predict(testCase), '(NO)')
