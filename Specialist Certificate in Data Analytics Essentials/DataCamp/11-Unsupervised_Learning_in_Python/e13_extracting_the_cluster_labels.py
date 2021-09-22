"""
Extracting the cluster labels
The hierarchical clustering has already been performed and mergings is the result of the linkage() function.
The list varieties gives the variety of each grain sample.

    Import:
        pandas as pd.
        fcluster from scipy.cluster.hierarchy.
    Perform a flat hierarchical clustering by using the fcluster() function on mergings. Specify a maximum height of 6
    and the keyword argument criterion='distance'.
    Create a DataFrame df with two columns named 'labels' and 'varieties', using labels and varieties, respectively,
    for the column values. This has been done for you.
    Create a cross-tabulation ct between df['labels'] and df['varieties'] to count the number of times each grain
    variety coincides with each cluster label.

"""

# Perform the necessary imports
import pandas as pd
from scipy.cluster.hierarchy import fcluster
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

varieties = ['Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Kama wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Rosa wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat',
             'Canadian wheat']
# Calculate the linkage: mergings
mergings = linkage(samples, method='single')

# print(mergings)
# Use fcluster to extract labels: labels
labels = fcluster(mergings, 6, criterion='distance')

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)
