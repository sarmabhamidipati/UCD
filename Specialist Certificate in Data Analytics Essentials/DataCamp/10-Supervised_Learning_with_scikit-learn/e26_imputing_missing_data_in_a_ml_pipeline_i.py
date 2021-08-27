"""
Imputing missing data in a ML Pipeline I
Instructions
100 XP

    Import Imputer from sklearn.preprocessing and SVC from sklearn.svm. SVC stands for
    Support Vector Classification, which is a type of SVM.
    Setup the Imputation transformer to impute missing data (represented as 'NaN') with the 'most_frequent'
    value in the column (axis=0).
    Instantiate a SVC classifier. Store the result in clf.
    Create the steps of the pipeline by creating a list of tuples:
        The first tuple should consist of the imputation step, using imp.
        The second should consist of the classifier.

"""

# Import the Imputer module
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# Setup the Imputation transformer: imp
imp = SimpleImputer(missing_values='NaN', strategy='most_frequent')

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp),
        ('SVM', clf)]
