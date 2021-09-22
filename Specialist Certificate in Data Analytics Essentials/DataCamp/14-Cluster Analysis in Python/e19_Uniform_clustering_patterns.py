"""
Uniform clustering patterns

"""

import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq

mouse = pd.read_csv('mouse.csv')
# print(comic_con)

# Use the linkage() function
distance_matrix = linkage(mouse[['x_scaled', 'y_scaled']], method='complete', metric='euclidean')

# Assign cluster labels
mouse['cluster_labels'] = fcluster(distance_matrix, 2, criterion='maxclust')

# Generate cluster centers
cluster_centers, distortion = kmeans(mouse[['x_scaled', 'y_scaled']], 3)

# Assign cluster labels
mouse['cluster_labels'], distortion_list = vq(mouse[['x_scaled', 'y_scaled']], cluster_centers)

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled',
                hue='cluster_labels', data=mouse)
plt.show()
