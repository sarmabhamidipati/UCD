"""
Clustering stocks using KMeans
In this exercise, you'll cluster companies using their daily stock price movements (i.e. the dollar difference between
the closing and opening prices for each trading day). You are given a NumPy array movements of daily price movements
from 2010 to 2015 (obtained from Yahoo! Finance), where each row corresponds to a company,
and each column corresponds to a trading day.
Instructions
100 XP

    Import Normalizer from sklearn.preprocessing.
    Create an instance of Normalizer called normalizer.
    Create an instance of KMeans called kmeans with 10 clusters.
    Using make_pipeline(), create a pipeline called pipeline that chains normalizer and kmeans.
    Fit the pipeline to the movements array.

"""
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# Import Normalizer
from sklearn.preprocessing import Normalizer


movements = np.array([[5.8000000e-01, -2.2000500e-01, -3.4099980e+00],
                      [-5.3599620e+00, 8.4001900e-01, -1.9589981e+01],
                      [-6.4000200e-01, -6.5000000e-01, -2.1000100e-01],
                      [-4.0001000e-02, -4.0000200e-01, 6.6000000e-01],
                      [-2.3500060e+00, 1.2600090e+00, -2.3500060e+00],
                      [4.7900090e+00, -1.7600090e+00, 3.7400210e+00],
                      [4.3000100e-01, 2.2999600e-01, 5.7000000e-01],
                      [-2.6000200e-01, 4.0000100e-01, 4.8000300e-01],
                      [9.0000000e-02, 1.0000000e-02, -8.0000000e-02],
                      [-3.0000000e-02, 2.0000000e-02, -3.0000000e-02],
                      [1.5999900e-01, 1.0001000e-02, 0.0000000e+00],
                      [-6.0001000e-02, 2.5999800e-01, 9.9998000e-02]])
# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer, kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)