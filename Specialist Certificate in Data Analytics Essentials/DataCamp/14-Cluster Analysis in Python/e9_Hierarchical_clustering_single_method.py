"""
Hierarchical clustering: single method
The data is stored in a Pandas data frame, comic_con. x_scaled and y_scaled are the column names of the standardized
X and Y coordinates of people at a given point in time.
Instructions
100 XP

    Import fcluster and linkage from scipy.cluster.hierarchy.
    Use the single method in the linkage() function.

"""
import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns

comic_con = pd.read_csv('comic_con.csv')
# print(comic_con)

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method='single', metric='euclidean')

# Assign cluster labels
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion='maxclust')

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled',
                hue='cluster_labels', data = comic_con)
plt.show()