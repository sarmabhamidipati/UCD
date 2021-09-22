"""
Search for the optimal tree
An untuned classification tree dt as well as the dictionary params_dt that you defined in the previous exercise are
available in your workspace.
Instructions
100 XP

    Import GridSearchCV from sklearn.model_selection.

    Instantiate a GridSearchCV object using 5-fold CV by setting the parameters:

        estimator to dt, param_grid to params_dt and

        scoring to 'roc_auc'.

"""

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# Set seed to 1 for reproducibility
SEED = 1
# Instantiate a DecisionTreeClassifier 'dt'
dt = DecisionTreeClassifier(random_state=SEED)

# Define params_dt
params_dt = {'max_depth': [2, 3, 4],
             'min_samples_leaf': [0.12, 0.14, 0.16, 0.18]
             }


# Instantiate grid_dt
grid_dt = GridSearchCV(estimator=dt,
                       param_grid=params_dt,
                       scoring='roc_auc',
                       cv=5,
                       n_jobs=-1)

