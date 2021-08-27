"""
Hyperparameter tuning with RandomizedSearchCV

Import DecisionTreeClassifier from sklearn.tree and RandomizedSearchCV from sklearn.model_selection.
Specify the parameters and distributions to sample from. This has been done for you.
Instantiate a DecisionTreeClassifier.
Use RandomizedSearchCV with 5-fold cross-validation to tune the hyperparameters:

    Inside RandomizedSearchCV(), specify the classifier, parameter distribution, and number of folds to use.
    Use the .fit() method on the RandomizedSearchCV object to fit it to the data X and y.

Print the best parameter and best score obtained from RandomizedSearchCV by accessing the
best_params_ and best_score_ attributes of tree_cv
"""
import pandas as pd
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

df = pd.read_csv('diabetes.csv')
# print(df.head())

X = pd.DataFrame(df['age'])
y = df['diabetes']

# Setup the parameters and distributions to sample from: param_dist
param_dist = {"max_depth": [3, None],
              "max_features": randint(1, 9),
              "min_samples_leaf": randint(1, 9),
              "criterion": ["gini", "entropy"]}

# Instantiate a Decision Tree classifier: tree
tree = DecisionTreeClassifier()

# Instantiate the RandomizedSearchCV object: tree_cv
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)

# Fit it to the data
tree_cv.fit(X, y)

# Print the tuned parameters and score
print("Tuned Decision Tree Parameters: {}".format(tree_cv.best_params_))
print("Best score is {}".format(tree_cv.best_score_))
