"""
How many dominant colors?
We have loaded the following image using the imread() function of the image class of matplotlib.
The RGB values are stored in a data frame, batman_df.
The RGB values have been standardized used the whiten() function, stored in columns, scaled_red, scaled_blue and scaled_green.

Construct an elbow plot with the data frame. How many dominant colors are present?
"""
# Import image class of matplotlib
import matplotlib.image as img
import pandas as pd
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.cluster.vq import whiten
import matplotlib.pyplot as plt
import seaborn as sns
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq


r = []
g = []
b = []

# Read batman image and print dimensions
batman_image = img.imread('batman.jpg')
print(batman_image.shape)

# Store RGB values of all pixels in lists r, g and b
for row in batman_image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

batman_df = pd.DataFrame({'red': r,
                          'blue': b,
                          'green': g})
print(batman_df.head())


# Scale wage and value
batman_df['scaled_red'] = whiten(batman_df['red'])
batman_df['scaled_blue'] = whiten(batman_df['blue'])
batman_df['scaled_green'] = whiten(batman_df['green'])


distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(batman_df[['scaled_red', 'scaled_blue', 'scaled_green']], i)
    distortions.append(distortion)

# Create a data frame with two lists, num_clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Create a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()