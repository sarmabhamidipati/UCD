"""
Clustering Wikipedia part I
Create a Pipeline object consisting of a TruncatedSVD followed by KMeans.
(This time, we've precomputed the word-frequency matrix for you, so there's no need for a TfidfVectorizer).

The Wikipedia dataset you will be working with was obtained from here.
Instructions
100 XP

    Import:
        TruncatedSVD from sklearn.decomposition.
        KMeans from sklearn.cluster.
        make_pipeline from sklearn.pipeline.
    Create a TruncatedSVD instance called svd with n_components=50.
    Create a KMeans instance called kmeans with n_clusters=6.
    Create a pipeline called pipeline consisting of svd and kmeans.

"""

# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)
