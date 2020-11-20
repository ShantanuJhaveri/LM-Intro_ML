import pandas as pd
import numpy as np

data = [[0, 0, 'A'], [1, 1, 'A'], [2, 3, 'B'], [2, 0, 'A'], [3, 4, 'B']]
df = pd.DataFrame(data)
df.columns = ['x1','x2','r']

import matplotlib.pyplot as plt
plt.scatter(df.loc[df.r == 'A', 'x1'], df.loc[df.r == 'A', 'x2'], color='r', label='A')
plt.scatter(df.loc[df.r == 'B', 'x1'], df.loc[df.r == 'B', 'x2'], color='b', label='B')

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.grid()

from sklearn import svm
model = svm.SVC(kernel='linear')
X = df[['x1','x2']]
y = df['r']
model.fit(X,y)

print('Weights w1 and w2:', model.coef_)
print('Bias:', model.intercept_)

w = model.coef_[0]
b_1 = -w[0] / w[1]
b_0 = model.intercept_[0]

xx = np.linspace(0,4)
yy = b_1 * xx - (b_0/w[1])
plt.plot(xx,yy, color='g')
plt.show()

print(model.predict([[3,3]]))
print(model.predict([[4,0]]))
print(model.predict([[2,2]]))
print(model.predict([[1,2]]))
print(model.predict([[1.5,1.5]]))