"""
Imputing missing data in a ML Pipeline II
Instructions
100 XP

    Import the following modules:
        Imputer from sklearn.preprocessing and Pipeline from sklearn.pipeline.
        SVC from sklearn.svm.
    Create the pipeline using Pipeline() and steps.
    Create training and test sets. Use 30% of the data for testing and a random state of 42.
    Fit the pipeline to the training set and predict the labels of the test set.
    Compute the classification report.

"""
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# Import necessary modules
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# Read the CSV file into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# convert dataframe column to numpy array
X = df['fertility'].to_numpy()
y = df['life'].to_numpy()
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Setup the pipeline steps: steps
imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

steps = [('imputation', imp), ('SVM', SVC())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))
