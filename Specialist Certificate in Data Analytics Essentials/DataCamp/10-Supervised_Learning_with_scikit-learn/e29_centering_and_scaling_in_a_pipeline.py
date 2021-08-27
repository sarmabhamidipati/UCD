"""
Centering and scaling in a pipeline
The feature array and target variable array have been pre-loaded as X and y. Additionally, KNeighborsClassifier and
train_test_split have been imported from sklearn.neighbors and sklearn.model_selection, respectively.

Instructions
100 XP

    Import the following modules:
        StandardScaler from sklearn.preprocessing.
        Pipeline from sklearn.pipeline.
    Complete the steps of the pipeline with StandardScaler() for 'scaler' and KNeighborsClassifier() for 'knn'.
    Create the pipeline using Pipeline() and steps.
    Create training and test sets, with 30% used for testing. Use a random state of 42.
    Fit the pipeline to the training set.
    Compute the accuracy scores of the scaled and unscaled models by using the .score() method inside
    the provided print() functions.

"""

# Import the necessary modules
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd


df = pd.read_csv('white-wine.csv')

X = df.drop('quality', axis=1).values

# if quality less than 5 then True else False
y = df['quality'].apply(lambda x: 'True' if x < 5 else 'False').to_numpy()


# Setup the pipeline steps: steps
steps = [('scaler', StandardScaler()),
         ('knn', KNeighborsClassifier())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the training set: knn_scaled
knn_scaled = pipeline.fit(X_train, y_train)

# Instantiate and fit a k-NN classifier to the unscaled data
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

# Compute and print metrics
print('Accuracy with Scaling: {}'.format(knn_scaled.score(X_test, y_test)))
print('Accuracy without Scaling: {}'.format(knn_unscaled.score(X_test, y_test)))
