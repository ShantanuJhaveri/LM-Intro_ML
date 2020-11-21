# Shantanu Jhaveri
# ITP 449 Fall 2020
# FINAL
# Question 1


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

# PT 1
# pd.set_option('display.max_columns', None)
wineDF = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                     '/Code_repo/final_exam/Jhaveri_Shantanu_Final_Q2/wineQualityReds.csv')

# PT 2
print('DIMENSION OF DF: ', wineDF.shape)

# PT 3
# print(wineDF.isnull())
# NO NULL THEREFORE NOTHING TO FILL IN

# PT 4/5
wineDF_TV = wineDF['quality']
wineDF = wineDF.drop(['quality', 'Wine'], axis=1)
scaler = StandardScaler()
scaler.fit(wineDF)
X = pd.DataFrame(scaler.transform(wineDF), columns=wineDF.columns)
y = wineDF_TV

# PT 6
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2020, stratify=y)
X_trainA, X_trainB, y_trainA, y_trainB = train_test_split(X_train, y_train, test_size=0.25, random_state=2020,
                                                          stratify=y_train)

# PT 7/8
# print(y_test.shape)
# print(X_test.shape)
print('THERE ARE 1,199 CASES IN THE TRAIN PARTITION')
print('THERE ARE 400 CASES IN THE TRAIN PARTITION')

# PT 9/10/11
kNN = KNeighborsClassifier()
neighbors = np.arange(1, 31)
trainA_Accuracy = np.empty(30)
trainB_Accuracy = np.empty(30)

for k in neighbors:
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(X_trainA, y_trainA)
    y_predict = kNN.predict(X_trainB)
    trainA_Accuracy[k - 1] = kNN.score(X_trainA, y_trainA)
    trainB_Accuracy[k - 1] = kNN.score(X_trainB, y_trainB)
    # print('(A) K= ', k, '; ACCURACY = ', accuracy_score(y_test, y_predict))

plt.figure(1)
plt.plot(neighbors, trainA_Accuracy, label='Training A Data (A)', marker='o')
plt.plot(neighbors, trainB_Accuracy, label='Training B Data (B)', marker='o')
plt.xticks(neighbors)
plt.title('kNN: Varying Number of Neighbors')
plt.xlabel('k = Number of Neighbors')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# PT 12
kNN = KNeighborsClassifier(n_neighbors=22)
kNN.fit(X_trainA, y_trainA)
y_predict = kNN.predict(X_test)
y_predictTrain = kNN.predict(X_trainA)

# PT 13
plt.figure(2)
plot_confusion_matrix(kNN, X_test, y_test)
plt.show()

# PT 14
print('FINAL MODEL (TRAIN) ACCURACY SCORE: ', accuracy_score(y_trainA, y_predictTrain))
# PT15
print('FINAL MODEL (TEST) ACCURACY SCORE: ', accuracy_score(y_test, y_predict))

# PT 16
testCase = [[8, 0.6, 0, 2.0, 0.076, 10, 30, 0.9978, 3.2, 0.5, 10.0]]
print('QUALITY OF [testCase] WINE:', kNN.predict(testCase))
