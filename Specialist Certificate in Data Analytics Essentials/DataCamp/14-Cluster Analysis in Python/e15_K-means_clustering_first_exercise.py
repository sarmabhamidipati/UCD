"""
K-means clustering: first exercise
This exercise will familiarize you with the usage of k-means clustering on a dataset. Let us use the Comic Con dataset
and check how k-means clustering works on it.

Recall the two steps of k-means clustering:

    Define cluster centers through kmeans() function. It has two required arguments: observations and number of clusters.
    Assign cluster labels through the vq() function. It has two required arguments: observations and cluster centers.

The data is stored in a Pandas data frame, comic_con. x_scaled and y_scaled are the column names of the
standardized X and Y coordinates of people at a given point in time.

Instructions
100 XP

    Import kmeans and vq functions in SciPy.
    Generate cluster centers using the kmeans() function with two clusters.
    Create cluster labels using these cluster centers.

"""

import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq

comic_con = pd.read_csv('comic_con.csv')
# print(comic_con)

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method='complete', metric='euclidean')

# Assign cluster labels
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion='maxclust')

# Generate cluster centers
cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], 2)

# Assign cluster labels
comic_con['cluster_labels'], distortion_list = vq(comic_con[['x_scaled', 'y_scaled']], cluster_centers)

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled',
                hue='cluster_labels', data=comic_con)
plt.show()
