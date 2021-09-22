"""
How many clusters of grain?

In the video, you learned how to choose a good number of clusters for a dataset using the k-means inertia graph.
You are given an array samples containing the measurements (such as area, perimeter, length, and several others) of
samples of grain. What's a good number of clusters in this case?

KMeans and PyPlot (plt) have already been imported for you.

This dataset was sourced from the UCI Machine Learning Repository.
"""

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

samples = np.array([[15.26, 14.84, 0.871, 3.312, 2.221, 5.22],
                    [14.88, 14.57, 0.8811, 3.333, 1.018, 4.956],
                    [14.29, 14.09, 0.905, 3.337, 2.699, 4.825],
                    [13.2, 13.66, 0.8883, 3.232, 8.315, 5.056],
                    [11.84, 13.21, 0.8521, 2.836, 3.598, 5.044],
                    [12.3, 13.34, 0.8684, 2.974, 5.637, 5.063]])
ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)

    # Fit model to samples
    model.fit(samples)

    # Append the inertia to the list of inertias
    model.inertia_
    inertias.append(model.inertia_)

# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()
