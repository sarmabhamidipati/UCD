"""
Linear regression vs regression tree
In this exercise, you'll compare the test set RMSE of dt to that achieved by a linear regression model.
We have already instantiated a linear regression model lr and trained it on the same dataset as dt.

The features matrix X_test, the array of labels y_test, the trained linear regression model lr, mean_squared_error
function which was imported under the alias MSE and rmse_dt from the previous exercise are available in your workspace.
Instructions
100 XP

    Predict test set labels using the linear regression model (lr) and assign the result to y_pred_lr.

    Compute the test set MSE and assign the result to mse_lr.

    Compute the test set RMSE and assign the result to rmse_lr.

"""
import import_data_for_supervised_learning1
# Import DecisionTreeRegressor from sklearn.tree
from sklearn.tree import DecisionTreeRegressor
# Import mean_squared_error from sklearn.metrics as MSE
from sklearn.metrics import mean_squared_error as MSE
from sklearn.linear_model import LinearRegression

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
# print("Test set RMSE of dt: {:.2f}".format(rmse_dt))

# lr = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
# lr needs to be defined.
# Predict test set labels
y_pred_lr = lr.predict(import_data_for_supervised_learning1.X_test)

# Compute mse_lr
mse_lr = MSE(import_data_for_supervised_learning1.y_test, y_pred_lr)

# Compute rmse_lr
rmse_lr = mse_lr**(1/2)

# Print rmse_lr
print('Linear Regression test set RMSE: {:.2f}'.format(rmse_lr))

# Print rmse_dt
print('Regression Tree test set RMSE: {:.2f}'.format(rmse_dt))
