"""
Evaluate the 10-fold CV error
In this exercise, you'll evaluate the 10-fold CV Root Mean Squared Error (RMSE) achieved by the regression tree dt
that you instantiated in the previous exercise.

In addition to dt, the training data including X_train and y_train are available in your workspace.
We also imported cross_val_score from sklearn.model_selection.

Note that since cross_val_score has only the option of evaluating the negative MSEs,
its output should be multiplied by negative one to obtain the MSEs.
The CV RMSE can then be obtained by computing the square root of the average MSE.
Instructions
100 XP

    Compute dt's 10-fold cross-validated MSE by setting the scoring argument to 'neg_mean_squared_error'.

    Compute RMSE from the obtained MSE scores.

"""

import pandas as pd
# Import train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score

auto = pd.read_csv('auto.csv')

df1 = pd.get_dummies(auto.origin, prefix='origin')

auto = auto.join(df1)
# print(auto.info())
# print(auto.head())

# Getting Features
X = auto[['displ', 'hp', 'weight', 'accel', 'size', 'origin_Asia', 'origin_Europe', 'origin_US']]

# Getting Predicting Value
y = auto['mpg']

# Set SEED for reproducibility
SEED = 1

# Split the data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Instantiate a DecisionTreeRegressor dt
dt = DecisionTreeRegressor(max_depth=4,min_samples_leaf=0.26, random_state=SEED)

# Compute the array containing the 10-folds CV MSEs
MSE_CV_scores = - cross_val_score(dt, X_train, y_train, cv=10,
                                  scoring='neg_mean_squared_error',
                                  n_jobs=-1)

# Compute the 10-folds CV RMSE
RMSE_CV = (MSE_CV_scores.mean())**(1/2)

# Print RMSE_CV
print('CV RMSE: {:.2f}'.format(RMSE_CV))