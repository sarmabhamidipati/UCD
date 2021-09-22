"""
Display dominant colors
To display the dominant colors, convert the colors of the cluster centers to their raw values and then converted them
to the range of 0-1, using the following formula: converted_pixel = standardized_pixel * pixel_std / 255

The RGB values are stored in a data frame, batman_df. The scaled RGB values are stored in columns, scaled_red,
scaled_blue and scaled_green. The cluster centers are stored in the variable cluster_centers,
which were generated using the kmeans() function with three clusters.
"""
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

# Get standard deviations of each color
r_std, g_std, b_std = batman_df[['red', 'green', 'blue']].std()

colors = []
for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    # Convert each standardized value to scaled value
    colors.append((
        scaled_r * r_std / 255,
        scaled_g * g_std / 255,
        scaled_b * b_std / 255
    ))

# Display colors of cluster centers
plt.imshow([colors])
plt.show()