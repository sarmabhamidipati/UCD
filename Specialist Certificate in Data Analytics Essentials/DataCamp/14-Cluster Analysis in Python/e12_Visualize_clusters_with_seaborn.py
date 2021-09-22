"""
Visualize clusters with seaborn
Let us now visualize the footfall dataset from Comic Con using the seaborn module. Visualizing clusters using seaborn
is easier with the inbuild hue function for cluster labels.

The data is stored in a Pandas data frame, comic_con. x_scaled and y_scaled are the column names of the standardized
X and Y coordinates of people at a given point in time. cluster_labels has the cluster labels. A linkage object
is stored in the variable distance_matrix.
"""

import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns

comic_con = pd.read_csv('comic_con.csv')
# print(comic_con)

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method='complete', metric='euclidean')

# Assign cluster labels
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion='maxclust')

# Define a colors dictionary for clusters
colors = {1: 'red', 2: 'blue'}

# Plot a scatter plot using seaborn
sns.scatterplot(x='x_scaled',
                y='y_scaled',
                hue='cluster_labels',
                data=comic_con)
plt.show()
