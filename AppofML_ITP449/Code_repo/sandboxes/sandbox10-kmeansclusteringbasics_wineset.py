import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
wine_df = pd.read_csv('/Users/shantanujhaveri/Desktop/work-git/GitHub/Learning-Modules_introML/AppofML_ITP449'
                      '/Code_repo/sandboxes/sandbox-data/wineQualityReds.csv')
wine_df.drop(wine_df.columns[0],axis=1,inplace=True)

print(wine_df.head())
print(wine_df.shape)

# plt.hist(wine_df['quality'])
# plt.show()

print(wine_df.groupby('quality').mean())
wine_df_normals = (wine_df - wine_df.min())/(wine_df.max()-wine_df.min())
print(wine_df_normals.head())

from sklearn.cluster import AgglomerativeClustering
clusters = AgglomerativeClustering(n_clusters=6).fit(wine_df_normals)

clusterLabels = pd.Series(clusters.labels_)

plt.hist(clusterLabels)
plt.title("Histogram of Cluster Label")
plt.xlabel("Cluster")
plt.ylabel("Frequency")
plt.show()

wine_df_normals['cluster'] = clusterLabels
print(wine_df_normals.groupby('cluster').mean())
print(wine_df_normals)