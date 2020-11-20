import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
iris_df = pd.read_csv(
    '/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo/sandboxes'
    '/sandbox-data/iris.csv')

iris_df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width','Species']
X = iris_df[['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']]
y = iris_df['Species']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=2020,stratify=y)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(X_train, y_train)

y_predict = dt.predict(X_test)

from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test,y_predict)
print(cnf_matrix)

print('Accuracy :', metrics.accuracy_score(y_test,y_predict))

metrics.plot_confusion_matrix(dt, X_test, y_test)
plt.show()

from sklearn import tree

plt.figure(2)
fn = X.columns
cn = y.unique()
irisTree = tree.plot_tree(dt, feature_names=fn,class_names=cn, filled=True)
plt.show()

print('Feature Importance:', dt.feature_importances_)