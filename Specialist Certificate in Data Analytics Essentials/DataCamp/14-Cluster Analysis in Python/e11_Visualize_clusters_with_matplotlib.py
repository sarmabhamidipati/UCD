"""
Visualize clusters with matplotlib
We have discussed that visualizations are necessary to assess the clusters that are formed and spot trends in your data.
Let us now focus on visualizing the footfall dataset from Comic-Con using the matplotlib module.

The data is stored in a Pandas data frame, comic_con. x_scaled and y_scaled are the column names of the standardized
X and Y coordinates of people at a given point in time. cluster_labels has the cluster labels.
A linkage object is stored in the variable distance_matrix.

Instructions
70 XP

    Import the pyplot class from matplotlib module as plt.
    Define a colors dictionary for two cluster labels, 1 and 2.
    Plot a scatter plot with colors for each cluster as defined by the colors dictionary.

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
colors = {1:'red', 2:'blue'}

# Plot a scatter plot
comic_con.plot.scatter(x='x_scaled',
                	   y='y_scaled',
                       c=comic_con['cluster_labels'].apply(lambda x: colors[x]))
plt.show()