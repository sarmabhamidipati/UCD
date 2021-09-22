"""
FIFA 18: defenders revisited
These are typically defense-minded players. In this exercise, you will perform clustering based on these attributes in
the data.

The following modules have been pre-loaded: kmeans, vq from scipy.cluster.vq, matplotlib.pyplot as plt, seaborn as sns.
The data for this exercise is stored in a Pandas dataframe, fifa. The scaled variables are scaled_def and scaled_phy.

Initialize the random seed to the list [1000,2000].
Fit the scaled data in columns scaled_def and scaled_phy into a k-means clustering algorithm with 3
clusters and assign cluster labels.
Display cluster centers of each cluster with respect to the scaled columns by
calculating the mean value for each cluster.

Create a seaborn scatter plot with scaled_def on the x-axis and scaled_phy on the y-axis,
with each cluster represented by a different color.
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
fifa['scaled_def'] = whiten(fifa['def'])
fifa['scaled_phy'] = whiten(fifa['phy'])

# Set up a random seed in numpy
random.seed([1000, 2000])

# Fit the data into a k-means algorithm
cluster_centers, _ = kmeans(fifa[['scaled_def', 'scaled_phy']], 3)

# Assign cluster labels
fifa['cluster_labels'], _ = vq(fifa[['scaled_def', 'scaled_phy']], cluster_centers)

# Display cluster centers
print(fifa[['scaled_def', 'scaled_phy', 'cluster_labels']].groupby('cluster_labels').mean())

# Plot clusters
sns.scatterplot(x='scaled_def', y='scaled_phy',
                hue='cluster_labels', data=fifa)
plt.show()
