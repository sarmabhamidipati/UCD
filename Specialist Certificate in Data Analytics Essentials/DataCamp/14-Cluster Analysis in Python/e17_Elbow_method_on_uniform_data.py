"""
Elbow method on uniform data
The data is stored in a Pandas data frame, uniform_data. x_scaled and y_scaled are the column names of the standardized
X and Y coordinates of points.

Instructions 1/2

    Create a list of distortions for each cluster in num_clusters.
    Create a data frame elbow_plot with num_clusters and distortions.
    With the .lineplot() method, plot elbow_plot with num_clusters in the x axis and distortions in the y axis.

"""

import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq

uniform_data = pd.read_csv('uniform_data.csv')
# print(uniform_data)

distortions = []
num_clusters = range(2, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(uniform_data[['x_scaled', 'y_scaled']], i)
    distortions.append(distortion)

# Create a data frame with two lists - number of clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
plt.xticks(num_clusters)
plt.show()