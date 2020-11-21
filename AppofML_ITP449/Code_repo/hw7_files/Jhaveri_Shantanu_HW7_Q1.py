# Shantanu Jhaveri
# ITP 449 Fall 2020
# HW7
# Question 1

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans

# PART 1/2 IMPORT DATA AND DROP WINE
pd.set_option('display.max_columns', None)
df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449/Code_repo'
                 '/hw7_files/wineQualityReds.csv')
df_winecluster = df[['Wine', 'quality']]
df = df.drop(columns=['Wine'])

# PART 3/4 EXTRACT QUALITY AND STORE IT IN A SEPARATE VARzIABLE AND DROP
qual = df['quality']
df = df.drop(columns=['quality'])
# X = df.iloc[:, 0:11]
# y = df.iloc[:, 11]

# PART 5 PRINT
# print(X)
# print(y)
print('\nDATAFRAME W/OUT QUALITY AND WINE:\n', df)
print('\nDATAFRAME WITH JUST QUALITY\n', qual)

# PART 6/7 NORMALIZE
myNorm = Normalizer()
df = pd.DataFrame(myNorm.transform(df), columns=df.columns)
print('\nNORMALIZED DATA:\n', df.head())

# PART 8 CREATE A RANGE OF K VALUES
neighbors_range = np.arange(1, 11)
inertia = []

# PART 9 PLOTTING
for k in neighbors_range:
    clusters = KMeans(n_clusters=k).fit(df)
    inertia.append(clusters.inertia_)

plt.plot(neighbors_range, inertia, marker='o')
plt.ylabel('Inertia')
plt.xlabel('Number of Clusters, k')
plt.xticks(neighbors_range)
plt.show()

# PART 10: 6 CLUSTERS
# PART 11A
kmeans = KMeans(n_clusters=6, random_state=2020)
y_kmeans = kmeans.fit_predict(df)
df['cluster'] = y_kmeans
# PART 11B
df_winecluster['cluster'] = y_kmeans
print('\nWINES WITH CORRESPONDING QUAL AND CLUSTER:\n', df_winecluster)
# PART 12
df['quality'] = qual
# PART 13
print('\nCROSSTAB OF QUALITY TO CLUSTER:\n', pd.crosstab(df['quality'], df['cluster']))
