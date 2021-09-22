"""
Basic checks on clusters
In the FIFA 18 dataset, we have concentrated on defenders in previous exercises. Let us try to focus on
attacking attributes of a player. Pace (pac), Dribbling (dri) and Shooting (sho) are features that are
present in attack minded players. In this exercise, k-means clustering has already been applied on the data
using the scaled values of these three attributes. Try some basic checks on the clusters so formed.

The data is stored in a Pandas data frame, fifa. The scaled column names are present in a list scaled_features.
The cluster labels are stored in the cluster_labels column. Recall the .count() and .mean() methods in Pandas
help you find the number of observations and mean of observations in a data frame.
"""

import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq
from scipy.cluster.vq import whiten
from numpy import random

fifa = pd.read_csv('fifa_18_sample_data.csv')

# print(fifa.head(10))

# Scale wage and value
fifa['scaled_pac'] = whiten(fifa['pac'])
fifa['scaled_dri'] = whiten(fifa['dri'])
fifa['scaled_sho'] = whiten(fifa['sho'])

scaled_features = ['scaled_pac', 'scaled_dri', 'scaled_sho']

# Fit the data into a k-means algorithm
cluster_centers, _ = kmeans(fifa[['scaled_pac', 'scaled_dri', 'scaled_sho']], 3)

# Assign cluster labels
fifa['cluster_labels'], _ = vq(fifa[scaled_features], cluster_centers)

# Assign cluster labels and print cluster centers
fifa['cluster_labels'], _ = vq(fifa[scaled_features], cluster_centers)
print(fifa.groupby('cluster_labels')[scaled_features].mean())

# Plot cluster centers to visualize clusters
fifa.groupby('cluster_labels')[scaled_features].mean().plot(legend=True, kind='bar')
plt.show()

# Get the name column of first 5 players in each cluster
for cluster in fifa['cluster_labels'].unique():
    print(cluster, fifa[fifa['cluster_labels'] == cluster]['name'].values[:5])