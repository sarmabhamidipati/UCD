"""
Pokémon sightings: hierarchical clustering
In this exercise, you will form two clusters of the sightings using hierarchical clustering.

'x' and 'y' are columns of X and Y coordinates of the locations of sightings, stored in a Pandas data frame, df.
The following are available for use: matplotlib.pyplot as plt, seaborn as sns, and pandas as pd.


    Import the linkage and fcluster libraries.
    Use the linkage() function to compute distances using the ward method.
    Generate cluster labels for each data point with two clusters using the fcluster() function.
    Plot the points with seaborn and assign a different color to each cluster.

"""
from matplotlib import pyplot as plt
import seaborn as sns, pandas as pd
# Import linkage and fcluster functions
from scipy.cluster.hierarchy import linkage, fcluster

x = [9, 6, 2, 3, 1, 7, 1, 6, 1, 7, 23, 26, 25, 23, 21, 23, 23, 20, 30, 23]
y = [8, 4, 10, 6, 0, 4, 10, 10, 6, 1, 29, 25, 30, 29, 29, 30, 25, 27, 26, 30]


df = pd.DataFrame({'x': x, 'y': y})

print(df)


# Use the linkage() function to compute distance
Z = linkage(df, 'ward')

# Generate cluster labels
df['cluster_labels'] = fcluster(Z, 2, criterion='maxclust')

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()
