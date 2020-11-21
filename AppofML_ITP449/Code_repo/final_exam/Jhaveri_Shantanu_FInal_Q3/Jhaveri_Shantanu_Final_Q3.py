# Shantanu Jhaveri
# ITP 449 Fall 2020
# FINAL
# Question 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# PT 1
pd.set_option('display.max_columns', None)
stores_df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                        '/Code_repo/final_exam/Jhaveri_Shantanu_FInal_Q3/Stores.csv')
# print(stores_df.info())
# print(stores_df.isnull())
# print(stores_df.isnull().sum())
storeNames = stores_df['Store']
stores_df = stores_df.drop(['Store'], axis=1)
scaler = StandardScaler()
scaler.fit(stores_df)
stores_df = pd.DataFrame(scaler.transform(stores_df), columns=stores_df.columns)

# PT 2
neighbors_range = np.arange(1, 11)
inertia = []
for k in neighbors_range:
    clusters = KMeans(n_clusters=k).fit(stores_df)
    inertia.append(clusters.inertia_)


# PT 3
plt.figure(1)
plt.title('Inertia v K')
plt.plot(neighbors_range, inertia, marker='o')
plt.ylabel('Inertia')
plt.xlabel('Number of Clusters, k')
plt.xticks(neighbors_range)
plt.show()

# PT 4
print('BEST K = 6')

# PT 5
kmeans = KMeans(n_clusters=6, random_state=2020)
y_kmeans = kmeans.fit_predict(stores_df)
testCase = [[4.1,3.5,2.4,0.5]]
testCase_Predict = kmeans.predict(testCase)
print('THE TEST CASE THAT WAS PRESENTED BELONGS TO CLUSTER: ', testCase_Predict)

# PT 6
stores_df['Cluster'] = y_kmeans
stores_df['Store'] = storeNames

# PT 7
plt.figure(2)
plt.hist(stores_df['Cluster'])
plt.title('Cluster Histogram')
plt.xlabel('Cluster Number')
plt.ylabel('Frequency')
plt.show()
