"""
Create a dendrogram
Dendrograms are branching diagrams that show the merging of clusters as we move through the distance matrix.
Let us use the Comic Con footfall data to create a dendrogram.

The data is stored in a Pandas data frame, comic_con. x_scaled and y_scaled are the column names of the standardized
X and Y coordinates of people at a given point in time. cluster_labels has the cluster labels. A linkage object
is stored in the variable distance_matrix.
Instructions
100 XP

    Import the dendrogram function from scipy.cluster.hierarchy.
    Create a dendrogram using the linkage object.
    Display the dendrogram using .show() method of the plt object.

"""

# Import the dendrogram function
from scipy.cluster.hierarchy import dendrogram
import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns

comic_con = pd.read_csv('comic_con.csv')
# print(comic_con)

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method='complete', metric='euclidean')


# Create a dendrogram
dn = dendrogram(distance_matrix)

# Display the dendogram
plt.show()