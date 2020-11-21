# Shantanu Jhaveri
# ITP 449 Fall 2020
# Final Project
# Q1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix


# pd.set_option('display.max_columns', None)
wine_df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                      '/Code_repo/finalproject_files/project_data/winequality.csv')
wine_df_qual = wine_df['Quality']
wine_df = wine_df.drop(['Quality'], axis=1)

# standardize data
scaler = StandardScaler()
scaler.fit(wine_df)
X = pd.DataFrame(scaler.transform(wine_df), columns=wine_df.columns)
y = wine_df_qual

# partition
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=2020, stratify=y)
X_trainA, X_trainB, y_trainA, y_trainB = train_test_split(X_train, y_train, test_size=0.25, random_state=2020,
                                                          stratify=y_train)

# build KNN
kNN = KNeighborsClassifier()

# plot
neighbors = np.arange(1,31)
train_Accuracy = np.empty(30)
test_Accuracy = np.empty(30)


for k in neighbors:
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(X_trainA, y_trainA)
    y_predict = kNN.predict(X_trainB)
    train_Accuracy[k - 1] = kNN.score(X_trainA, y_trainA)
    test_Accuracy[k - 1] = kNN.score(X_trainB, y_trainB)
    # print('(A) K= ', k, '; ACCURACY = ', accuracy_score(y_test, y_predict))

plt.figure(1)
plt.plot(neighbors, train_Accuracy, label='Training Accuracy (A)', marker='o')
plt.plot(neighbors, test_Accuracy, label='Testing Accuracy (B)', marker='o')
plt.xticks(neighbors)
plt.title('kNN: Varying Number of Neighbors')
plt.xlabel('k = Number of Neighbors')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# k = 4 GIVES THE HIGHEST ACCURACY, HOWEVER, PROF. TOLD US TO USE THE HIGHEST K FOR THE X_TRAINB DATA WHICH IS 27
kNN = KNeighborsClassifier(n_neighbors=4)
kNN.fit(X_trainA,y_trainA)
y_predict = kNN.predict(X_test)
print('\nPRINTED CONFUSION MATRIX:\n', confusion_matrix(y_test, y_predict))
plt.figure(2)
plot_confusion_matrix(kNN, X_test, y_test)
plt.show()

X_test_dfcopy = X_test.copy()
X_test_dfcopy['Quality'] = y_test
X_test_dfcopy['Predicted Quality'] = y_predict
print(X_test_dfcopy)

print('FINAL MODEL ACCURACY SCORE: ',accuracy_score(y_test, y_predict))
