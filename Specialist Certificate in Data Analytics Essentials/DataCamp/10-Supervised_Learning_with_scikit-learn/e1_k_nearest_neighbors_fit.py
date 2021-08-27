"""
k-Nearest Neighbors: Fit
Having explored the Congressional voting records dataset, it is time now to build your first classifier.
In this exercise, you will fit a k-Nearest Neighbors classifier to the voting dataset, which has once again been
pre-loaded for you into a DataFrame df.

In the video, Hugo discussed the importance of ensuring your data adheres to the format required by
the scikit-learn API. The features need to be in an array where each column is a feature and each row a different
observation or data point - in this case, a Congressman's voting record. The target needs to be a single column
with the same number of observations as the feature data. We have done this for you in this exercise.
Notice we named the feature array X and response variable y:
This is in accordance with the common scikit-learn practice.

Your job is to create an instance of a k-NN classifier with 6 neighbors (by specifying the n_neighbors parameter) and
then fit it to the data. The data has been pre-loaded into a DataFrame called df.
"""
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

df = pd.read_csv('df.csv')
# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)