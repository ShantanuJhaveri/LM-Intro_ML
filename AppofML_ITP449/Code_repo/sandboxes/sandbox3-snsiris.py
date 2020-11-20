import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pydataset import data

iris = sns.load_dataset('iris')
X_iris = iris.drop('species', axis=1)
y_iris = iris['species']
sns.pairplot(iris, hue='species')
plt.show()
# print(iris.head())
# print(X_iris.head())
# print(y_iris.head())
