import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pd.set_option('display.max_columns', None)
wine_df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                      '/Code_repo/sandboxes/sandbox-data/wineQualityReds.csv')
sb.countplot(x='quality', data=wine_df)
plt.show()
wine_df.drop(wine_df.columns[0], axis=1, inplace=True)

X = wine_df.iloc[:, 0:11]
y = wine_df.iloc[:, 11]

# Normalize the data
from sklearn.preprocessing import Normalizer

myNorm = Normalizer(norm='l2')
X = pd.DataFrame(myNorm.transform(X), columns=X.columns)
print(X.head())

# Partitions
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020, stratify=y)

# range of K neighbors
neighbors = np.arange(1, 21)
trainAccuracy = np.empty(20)
testAccuracy = np.empty(20)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

for k in neighbors:
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(X_train, y_train)
    y_predict = kNN.predict(X_test)
    cnf_matrix = confusion_matrix(y_test, y_predict)
    trainAccuracy[k - 1] = kNN.score(X_train, y_train)
    testAccuracy[k - 1] = kNN.score(X_test, y_test)

from sklearn.metrics import plot_confusion_matrix

plt.plot(neighbors, testAccuracy, label='Testing Accuracy')
plt.plot(neighbors, trainAccuracy, label='Training Accuracy')
plt.xticks(neighbors)
plt.legend()
plt.title('kNN: Varying Number of Neighbors')
plt.xlabel('k = Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
