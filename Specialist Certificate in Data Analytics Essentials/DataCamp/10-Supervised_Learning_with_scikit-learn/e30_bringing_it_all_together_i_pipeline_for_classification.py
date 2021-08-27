"""
Bringing it all together I: Pipeline for classification
The following modules and functions have been pre-loaded: Pipeline, SVC, train_test_split, GridSearchCV,
classification_report, accuracy_score. The feature and target variable arrays X and y have also been pre-loaded.

Instructions
100 XP

    Setup the pipeline with the following steps:
        Scaling, called 'scaler' with StandardScaler().
        Classification, called 'SVM' with SVC().
    Specify the hyperparameter space using the following notation: 'step_name__parameter_name'.
    Here, the step_name is SVM, and the parameter_names are C and gamma.
    Create training and test sets, with 20% of the data used for the test set. Use a random state of 21.
    Instantiate GridSearchCV with the pipeline and hyperparameter space and fit it to the training set.
    Use 3-fold cross-validation (This is the default, so you don't have to specify it).
    Predict the labels of the test set and compute the metrics. The metrics have been computed for you.

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
from sklearn.svm import SVC
from sklearn.metrics import classification_report


df = pd.read_csv('white-wine.csv')

X = df.drop('quality', axis=1).values

# if quality less than 5 then True else False
y = df['quality'].apply(lambda x: 'True' if x < 5 else 'False').to_numpy()


# Setup the pipeline
steps = [('scaler', StandardScaler()), ('SVM', SVC())]

pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'SVM__C':[1, 10, 100],
              'SVM__gamma':[0.1, 0.01]}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=21)

# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline, param_grid=parameters, cv=3)

# Fit to the training set
cv.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)

# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))

