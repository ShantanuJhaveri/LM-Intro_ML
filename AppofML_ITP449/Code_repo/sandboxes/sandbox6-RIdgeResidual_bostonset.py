import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

pd.set_option('display.max_columns', None)
boston = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                     '/Code_repo/sandboxes/sandbox-data/BostonHousing.csv')
bostonNUM = boston.drop(['CHAS'], axis=1)
# EDIT TO MAKE EVERYTHING A FLOAT
bostonNUM['RAD'] = bostonNUM['RAD'].astype(float)
bostonNUM['TAX'] = bostonNUM['TAX'].astype(float)

# PAIRPLOT TO IDENTIFY VARIABLES
# sb.pairplot(bostonNUM)
# plt.show()

# REMOVE NON CORRELATIONAL VARIABLES AND DATA
bostonNUM2 = bostonNUM.drop(['AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO'], axis=1)
# FIND THE 3 BEST VARIABLES
# sb.pairplot(bostonNUM2[['RM', 'B', 'LSTAT', 'MEDV']], kind='reg')
# REGRESSION MODEL FOR THE STRONGEST
bostonNUMF = bostonNUM[['LSTAT', 'MEDV']]

model = LinearRegression()
# I MADE THIS A NPARRAY BECAUSE IT PREVENTS AN ERROR WHEN CONVERTING BIG_X INTO A 2D ARRAY
x = np.array(bostonNUMF['LSTAT'])
X = x[:,np.newaxis]
y = bostonNUMF['MEDV']
model.fit(X,y)

y_predicted = model.predict(X)
plt.scatter(x,y, color='r')
plt.plot(x,y_predicted, color='g')
plt.show()


# PLOTTING RESIDUALS TO CHECK ACCURACY
from sklearn.linear_model import Ridge
from yellowbrick.regressor import ResidualsPlot

x = boston['LSTAT'].values
# RESHAPING JUST INCASE THE ARRAY IS NOT A 2D ARRAY
X = x.reshape(-1,1)
y = boston['MEDV']

ridge = Ridge()
visualizer = ResidualsPlot(ridge)
visualizer.fit(X,y)
visualizer.show()