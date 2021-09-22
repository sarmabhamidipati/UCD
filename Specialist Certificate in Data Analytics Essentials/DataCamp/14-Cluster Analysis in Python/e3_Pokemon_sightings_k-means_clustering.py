"""
Pokémon sightings: k-means clustering
Just like the previous exercise, we will use the same example of Pokémon sightings. In this exercise,
you will form clusters of the sightings using k-means clustering.

x and y are columns of X and Y coordinates of the locations of sightings, stored in a Pandas data frame, df. T
he following are available for use: matplotlib.pyplot as plt, seaborn as sns, and pandas as pd.
"""

from matplotlib import pyplot as plt
import seaborn as sns, pandas as pd
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq

x = [9, 6, 2, 3, 1, 7, 1, 6, 1, 7, 23, 26, 25, 23, 21, 23, 23, 20, 30, 23]
y = [8, 4, 10, 6, 0, 4, 10, 10, 6, 1, 29, 25, 30, 29, 29, 30, 25, 27, 26, 30]

df = pd.DataFrame({'x': x, 'y': y})

df['x'] = df.astype(float)

print(df.dtypes)

# Compute cluster centers
centroids, _ = kmeans(df, 2)

# Assign cluster labels
df['cluster_labels'], _ = vq(df, centroids)

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()
