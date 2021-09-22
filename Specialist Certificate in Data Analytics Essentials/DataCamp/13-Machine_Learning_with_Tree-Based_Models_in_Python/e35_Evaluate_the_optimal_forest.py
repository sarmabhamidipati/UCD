"""
Evaluate the optimal forest
In this last exercise of the course, you'll evaluate the test set RMSE of grid_rf's optimal model.

The dataset is already loaded and processed for you and is split into 80% train and 20% test.
In your environment are available X_test, y_test and the function mean_squared_error from sklearn.metrics
under the alias MSE. In addition, we have also loaded the trained GridSearchCV object grid_rf that you
instantiated in the previous exercise. Note that grid_rf was trained as follows:

grid_rf.fit(X_train, y_train)
Instructions
100 XP

    Import mean_squared_error as MSE from sklearn.metrics.

    Extract the best estimator from grid_rf and assign it to best_model.

    Predict best_model's test set labels and assign the result to y_pred.

    Compute best_model's test set RMSE.

"""

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error as MSE
# Import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('bikes.csv')
# print(df.info())

df = df.dropna()

# print(df.info())

X = df.drop('cnt', axis=1)
y = df['cnt']
# print(X.head())
# print(y.head())


# Set seed for reproducibility
SEED = 1

# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

# Instantiate a random forests regressor 'rf'
rf = RandomForestRegressor(random_state=SEED)

# Define the dictionary 'params_rf'
params_rf = {'n_estimators': [100, 350, 500],
             'max_features': ['log2', 'auto', 'sqrt'],
             'min_samples_leaf': [2, 10, 30]
             }

# Instantiate grid_rf
grid_rf = GridSearchCV(estimator=rf,
                       param_grid=params_rf,
                       scoring='neg_mean_squared_error',
                       cv=3,
                       verbose=1,
                       n_jobs=-1)

# Fit 'grid_rf' to the training set
grid_rf.fit(X_train, y_train)

# Extract the best estimator
best_model = grid_rf.best_estimator_

# Predict test set labels
y_pred = best_model.predict(X_test)

# Compute rmse_test
rmse_test = MSE(y_test, y_pred)**(1/2)

# Print rmse_test
print('Test RMSE of best model: {:.3f}'.format(rmse_test))
