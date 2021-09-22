"""
NMF applied to Wikipedia articles

"""
import numpy as np
from sklearn.decomposition import NMF

articles = np.array([[0., 0., 0., 0., 0., 0.],
                     [0., 0., 0.02960744, 0., 0., 0.],
                     [0., 0., 0., 0.01159441, 0., 0.],
                     [0., 0., 0., 0., 0., 0.],
                     [0., 0.00610985, 0., 0., 0.00547551, 0.],
                     [0., 0., 0., 0., 0., 0.]])
# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

# Print the NMF features
print(nmf_features.round(2))
