"""
FIFA 18: exploring defenders
The following modules are pre-loaded: dendrogram, linkage, fcluster from scipy.cluster.hierarchy,
matplotlib.pyplot as plt, seaborn as sns. The data is stored in a Pandas dataframe, fifa.

Assign cluster labels to each row in the data using the fcluster() function (use 3 clusters).

Display cluster centers of each cluster with respect to the scaled columns
by calculating the mean value for each cluster.

Create a scatter plot using seaborn with the scaled_sliding_tackle attribute on the x-axis and the scaled_aggression
attribute on the y-axis. Assign a different color to each cluster.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import fcluster, linkage
import seaborn as sns

fifa = pd.read_csv('fifa_18_sample_data.csv')

# Scale wage and value
fifa['scaled_sliding_tackle'] = whiten(fifa['sliding_tackle'])
fifa['scaled_aggression'] = whiten(fifa['aggression'])

fifa = fifa[['sliding_tackle', 'aggression', 'scaled_sliding_tackle', 'scaled_aggression']]

# print(fifa)
# Fit the data into a hierarchical clustering algorithm
distance_matrix = linkage(fifa[['scaled_sliding_tackle', 'scaled_aggression']], 'ward')

# Assign cluster labels to each row of data
fifa['cluster_labels'] = fcluster(distance_matrix, 3, criterion='maxclust')

# Display cluster centers of each cluster
print(fifa[['scaled_sliding_tackle',
            'scaled_aggression', 'cluster_labels']].groupby('cluster_labels').mean())

# Create a scatter plot through seaborn
sns.scatterplot(x='scaled_sliding_tackle', y='scaled_aggression', hue='cluster_labels', data=fifa)
plt.show()
