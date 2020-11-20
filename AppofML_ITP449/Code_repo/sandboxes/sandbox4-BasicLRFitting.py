import matplotlib.pyplot as plt
import numpy as np

x = 10 * np.random.rand(50)
y = 2 * x - 1 + np.random.rand(50)

# step one : import model
from sklearn.linear_model import LinearRegression

# step two: set parameters
model = LinearRegression(fit_intercept=True)
print(type(model))

# step three: arrange data
# print(x.shape)
# print(y.shape)
X = x[:, np.newaxis]
# print(X.shape)

# step four: Fit the model to the data
model.fit(X, y)
print(model.coef_)
print(model.intercept_)

# step five: predict for unknown data
xfit = np.linspace(-1, 11, num=50)
# print(xfit.shape)
Xfit = xfit[:, np.newaxis]
# print(Xfit.shape)
yfit = model.predict(Xfit)

plt.scatter(x, y)
plt.plot(Xfit, yfit, color='r')
plt.show()
