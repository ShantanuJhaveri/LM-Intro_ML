from pydataset import data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Data Import
pima = data('Pima.tr')
plt.scatter(pima.skin, pima.bmi)
plt.title('Basic Data Visualization')
plt.show()

# Test train split for supervised training
X_train, X_test, y_train, y_test = train_test_split(pima.skin, pima.bmi)
plt.scatter(X_train, y_train, label='Training Data', alpha=0.7, color='r')
plt.scatter(X_test, y_test, label='Testing Data', alpha=0.7, color='g')
plt.legend()
plt.title('Testing and Training Data Split')
plt.show()

# Applying model
LR = LinearRegression()
LR.fit(X_train.values.reshape(-1, 1), y_train.values)
prediction = LR.predict(X_test.values.reshape(-1, 1))
plt.plot(X_test, prediction, label="Linear Regression", color='b')
plt.scatter(X_test, y_test, label="Actual Testing Data", color='g')
plt.legend()
plt.show()

# Predict the BMI of woman with skinfold 50
# print(LR.predict(np.array([[50]]))[0])

# Score the model
score = LR.score(X_test.values.reshape(-1, 1), y_test.values)
print('Score = ', score)
