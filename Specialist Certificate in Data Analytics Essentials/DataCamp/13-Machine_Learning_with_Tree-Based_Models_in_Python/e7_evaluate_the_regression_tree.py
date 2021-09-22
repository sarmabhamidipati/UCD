"""
Evaluate the regression tree
In this exercise, you will evaluate the test set performance of dt using the Root Mean Squared Error (RMSE) metric.
The RMSE of a model measures, on average, how much the model's predictions differ from the actual labels.
The RMSE of a model can be obtained by computing the square root of the model's Mean Squared Error (MSE).

The features matrix X_test, the array y_test, as well as the decision tree regressor dt that you trained
in the previous exercise are available in your workspace.

Instructions
100 XP

    Import the function mean_squared_error as MSE from sklearn.metrics.
    Predict the test set labels and assign the output to y_pred.
    Compute the test set MSE by calling MSE and assign the result to mse_dt.
    Compute the test set RMSE and assign it to rmse_dt.

"""

import import_data_for_supervised_learning1
# Import DecisionTreeRegressor from sklearn.tree
from sklearn.tree import DecisionTreeRegressor
# Import mean_squared_error from sklearn.metrics as MSE
from sklearn.metrics import mean_squared_error as MSE

# Instantiate dt
dt = DecisionTreeRegressor(max_depth=8,
                           min_samples_leaf=0.13,
                           random_state=3)

# Fit dt to the training set
dt.fit(import_data_for_supervised_learning1.X_train, import_data_for_supervised_learning1.y_train)


# Compute y_pred
y_pred = dt.predict(import_data_for_supervised_learning1.X_test)

# Compute mse_dt
mse_dt = MSE(import_data_for_supervised_learning1.y_test, y_pred)

# Compute rmse_dt
rmse_dt = mse_dt**(1/2)

# Print rmse_dt
print("Test set RMSE of dt: {:.2f}".format(rmse_dt))