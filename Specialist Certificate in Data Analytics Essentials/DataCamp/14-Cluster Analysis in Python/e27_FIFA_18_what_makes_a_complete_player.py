"""
FIFA 18: what makes a complete player?
The overall level of a player in FIFA 18 is defined by six characteristics: pace (pac), shooting (sho),
passing (pas), dribbling (dri), defending (def), physical (phy).

Before you start the exercise, you may wish to explore scaled_features in the console to check out the list of
six scaled columns names.

Use the kmeans() algorithm to create 2 clusters using the list of columns, scaled_features.

"""

import pandas as pd
# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt
import seaborn as sns
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq
from scipy.cluster.vq import whiten
from numpy import random

fifa = pd.read_csv('fifa_18_sample_data.csv')

# print(fifa.head(10))

# Scale wage and value
fifa['scaled_pac'] = whiten(fifa['pac'])
fifa['scaled_sho'] = whiten(fifa['sho'])
fifa['scaled_pas'] = whiten(fifa['pas'])
fifa['scaled_dri'] = whiten(fifa['dri'])
fifa['scaled_def'] = whiten(fifa['def'])
fifa['scaled_phy'] = whiten(fifa['phy'])

scaled_features = ['scaled_pac',
                   'scaled_sho',
                   'scaled_pas',
                   'scaled_dri',
                   'scaled_def',
                   'scaled_phy']

# Fit the data into a k-means algorithm
cluster_centers, _ = kmeans(fifa[scaled_features], 2)

# Assign cluster labels
fifa['cluster_labels'], _ = vq(fifa[['scaled_pac','scaled_sho','scaled_pas','scaled_dri','scaled_def','scaled_phy']], cluster_centers)

# Assign cluster labels and print cluster centers
fifa['cluster_labels'], _ = ____
print(fifa.groupby(____)[____].____())