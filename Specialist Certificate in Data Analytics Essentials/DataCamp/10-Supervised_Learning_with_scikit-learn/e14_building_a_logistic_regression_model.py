"""
Building a logistic regression model
Time to build your first logistic regression model! As Hugo showed in the video, scikit-learn makes it very easy to try
different models, since the Train-Test-Split/Instantiate/Fit/Predict paradigm applies to all classifiers and
regressors - which are known in scikit-learn as 'estimators'. You'll see this now for yourself as you train a
logistic regression model on exactly the same data as in the previous exercise. Will it outperform k-NN?
There's only one way to find out!

The feature and target variable arrays X and y have been pre-loaded, and train_test_split has been imported
for you from sklearn.model_selection.
"""
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('diabetes.csv')
# print(df.head())

X = pd.DataFrame(df['age'])

y = df['diabetes']

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

# Create the classifier: logreg
logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = logreg.predict(X_test)

# Compute and print the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
