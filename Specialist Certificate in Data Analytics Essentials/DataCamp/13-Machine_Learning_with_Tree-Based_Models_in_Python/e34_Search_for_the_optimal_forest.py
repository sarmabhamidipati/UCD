"""
Search for the optimal forest
The untuned random forests regressor model rf as well as the dictionary params_rf that you defined in the previous
exercise are available in your workspace.
Instructions
100 XP

    Import GridSearchCV from sklearn.model_selection.

    Instantiate a GridSearchCV object using 3-fold CV by using negative mean squared error as the scoring metric.

"""
# Import GridSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error as MSE
# Import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

# Set seed for reproducibility
SEED = 1
# Instantiate a random forests regressor 'rf'
rf = RandomForestRegressor(random_state= SEED)

# Define the dictionary 'params_rf'
params_rf = {'n_estimators' : [100,350,500],
             'max_features' : ['log2', 'auto', 'sqrt'],
             'min_samples_leaf' : [2,10,30]
            }

# Instantiate grid_rf
grid_rf = GridSearchCV(estimator=rf,
                       param_grid=params_rf,
                       scoring='neg_mean_squared_error',
                       cv=3,
                       verbose=1,
                       n_jobs=-1)

