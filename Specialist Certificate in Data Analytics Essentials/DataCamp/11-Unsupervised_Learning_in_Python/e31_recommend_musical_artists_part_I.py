"""
Recommend musical artists part I

In this exercise and the next, you'll use what you've learned about NMF to recommend popular music artists!
You are given a sparse array artists whose rows correspond to artists and whose columns correspond to users.
The entries give the number of times each artist was listened to by each user.
"""
import numpy as np
# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline


artists = np.array([[0., 0., 105., 0., 0., 0.],
                    [128., 211., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 55., 0.],
                    [0., 0., 0., 0., 0., 0.]])


# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)

