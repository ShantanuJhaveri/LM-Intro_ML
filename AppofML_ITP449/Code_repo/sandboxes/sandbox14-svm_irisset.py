import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

pd.set_option('display.max_columns', None)
iris_df = pd.read_csv(
    '/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo/sandboxes/sandbox-data/iris.csv')
# print(iris_df.info())
# print(iris_df.Species.unique())
iris_df_sepal = iris_df.drop(columns=['Petal length', 'Petal width'])
plt.figure(1)
sb.scatterplot(data=iris_df_sepal, x='Sepal width', y='Sepal length', hue='Species') # Professor made this scatterplot
# in the most gross way possible, if time allots I will come back and add that
plt.show()
plt.figure(2)
iris_df_petal = iris_df.drop(columns=['Sepal length', 'Sepal width'])
sb.scatterplot(data=iris_df_petal, x='Petal width', y='Petal length', hue='Species')
plt.show()

X = iris_df[['Sepal length', 'Sepal width','Petal length', 'Petal width']]
y = iris_df['Species']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=2020,stratify=y)

from sklearn import svm
model = svm.SVC()
model.fit(X_train,y_train)
y_predict = model.predict(X_test)

from sklearn import metrics
print('Accuracy:',metrics.accuracy_score(y_test,y_predict))
plt.figure(3)
metrics.plot_confusion_matrix(model, X_test, y_test)
plt.show()