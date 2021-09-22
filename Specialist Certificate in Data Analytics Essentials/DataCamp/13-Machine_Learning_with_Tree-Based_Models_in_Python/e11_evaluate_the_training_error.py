"""
Evaluate the training error
You'll now evaluate the training set RMSE achieved by the regression tree dt that you
instantiated in a previous exercise.
Instructions
100 XP

    Import mean_squared_error as MSE from sklearn.metrics.
    Fit dt to the training set.
    Predict dt's training set labels and assign the result to y_pred_train.
    Evaluate dt's training set RMSE and assign it to RMSE_train.


"""


import pandas as pd
# Import train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error as MSE

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

# Fit dt to the training set
dt.fit(X_train, y_train)

# Predict the labels of the training set
y_pred_train = dt.predict(X_train)

# Evaluate the training set RMSE of dt
RMSE_train = (MSE(y_train, y_pred_train))**(1/2)

# Print RMSE_train
print('Train RMSE: {:.2f}'.format(RMSE_train))