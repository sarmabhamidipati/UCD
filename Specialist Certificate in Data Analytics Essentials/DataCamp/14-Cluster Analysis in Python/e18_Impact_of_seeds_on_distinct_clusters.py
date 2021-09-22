"""
Impact of seeds on distinct clusters
The data is stored in a Pandas data frame, comic_con. x_scaled and y_scaled are the column names of the
standardized X and Y coordinates of people at a given point in time.

Instructions 1/2

    Import the random class from numpy and initialize the seed with the integer 0.
"""

import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq

comic_con = pd.read_csv('comic_con.csv')
# print(comic_con)

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method='complete', metric='euclidean')

# Assign cluster labels
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion='maxclust')

# Initialize seed
# random.seed(0) step1
# step 2
random.seed([1, 2, 1000])

# Run kmeans clustering
cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], 2)
comic_con['cluster_labels'], distortion_list = vq(comic_con[['x_scaled', 'y_scaled']], cluster_centers)

# Plot the scatterplot
sns.scatterplot(x='x_scaled', y='y_scaled',
                hue='cluster_labels', data=comic_con)
plt.show()
