"""
Different linkage, different hierarchical clustering!
You are given an array samples. Each row corresponds to a voting country, and each column corresponds to a performance t
hat was voted for. The list country_names gives the name of each voting country.
This dataset was obtained from Eurovision.
Instructions
100 XP

    Import linkage and dendrogram from scipy.cluster.hierarchy.
    Perform hierarchical clustering on samples using the linkage() function with the method='single' keyword argument.
    Assign the result to mergings.
    Plot a dendrogram of the hierarchical clustering, using the list country_names as the labels.
    In addition, specify the leaf_rotation=90, and leaf_font_size=6 keyword arguments as you have done earlier.

"""
# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np

samples = np.array([[2., 12., 0., 0., 6., 0.],
                    [12., 0., 4., 0., 10., 0.],
                    [0., 12., 3., 0., 8., 4.],
                    [8., 5., 6., 12., 7., 0.],
                    [7., 4., 0., 0., 12., 0.],
                    [0., 6., 0., 0., 5., 12.],
                    [2., 12., 0., 0., 6., 0.],
                    [12., 0., 4., 0., 10., 0.],
                    [0., 12., 3., 0., 8., 4.],
                    [8., 5., 6., 12., 7., 0.],
                    [7., 4., 0., 0., 12., 0.],
                    [0., 6., 0., 0., 5., 12.],
                    [2., 12., 0., 0., 6., 0.],
                    [12., 0., 4., 0., 10., 0.],
                    [0., 12., 3., 0., 8., 4.],
                    [8., 5., 6., 12., 7., 0.],
                    [7., 4., 0., 0., 12., 0.],
                    [0., 6., 0., 0., 5., 12.],
                    [2., 12., 0., 0., 6., 0.],
                    [12., 0., 4., 0., 10., 0.],
                    [0., 12., 3., 0., 8., 4.],
                    [8., 5., 6., 12., 7., 0.],
                    [7., 4., 0., 0., 12., 0.],
                    [0., 6., 0., 0., 5., 12.],
                    [2., 12., 0., 0., 6., 0.],
                    [12., 0., 4., 0., 10., 0.],
                    [0., 12., 3., 0., 8., 4.],
                    [8., 5., 6., 12., 7., 0.],
                    [7., 4., 0., 0., 12., 0.],
                    [0., 6., 0., 0., 5., 12.],
                    [2., 12., 0., 0., 6., 0.],
                    [12., 0., 4., 0., 10., 0.],
                    [0., 12., 3., 0., 8., 4.],
                    [8., 5., 6., 12., 7., 0.],
                    [7., 4., 0., 0., 12., 0.],
                    [0., 6., 0., 0., 5., 12.],
                    [2., 12., 0., 0., 6., 0.],
                    [12., 0., 4., 0., 10., 0.],
                    [0., 12., 3., 0., 8., 4.],
                    [8., 5., 6., 12., 7., 0.],
                    [7., 4., 0., 0., 12., 0.],
                    [0., 6., 0., 0., 5., 12.]])

country_names = ['Albania',
                 'Armenia',
                 'Australia',
                 'Austria',
                 'Azerbaijan',
                 'Belarus',
                 'Belgium',
                 'Bosnia & Herzegovina',
                 'Bulgaria',
                 'Croatia',
                 'Cyprus',
                 'Czech Republic',
                 'Denmark',
                 'Estonia',
                 'F.Y.R. Macedonia',
                 'Finland',
                 'France',
                 'Georgia',
                 'Germany',
                 'Greece',
                 'Hungary',
                 'Iceland',
                 'Ireland',
                 'Israel',
                 'Italy',
                 'Latvia',
                 'Lithuania',
                 'Malta',
                 'Moldova',
                 'Montenegro',
                 'Norway',
                 'Poland',
                 'Russia',
                 'San Marino',
                 'Serbia',
                 'Slovenia',
                 'Spain',
                 'Sweden',
                 'Switzerland',
                 'The Netherlands',
                 'Ukraine',
                 'United Kingdom']

# Calculate the linkage: mergings
mergings = linkage(samples, method='single')

# Plot the dendrogram
dendrogram(mergings,
           labels=country_names,
           leaf_rotation=90,
           leaf_font_size=6)
plt.show()
