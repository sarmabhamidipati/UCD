"""
Evaluate the GB regressor
Now that the test set predictions are available, you can use them to evaluate the test set Root
Mean Squared Error (RMSE) of gb.

y_test and predictions y_pred are available in your workspace.

Instructions
100 XP

    Import mean_squared_error from sklearn.metrics as MSE.

    Compute the test set MSE and assign it to mse_test.

    Compute the test set RMSE and assign it to rmse_test.

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE
# Import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor


df = pd.read_csv('bikes.csv')
df = df.dropna()


X = df.drop('cnt', axis=1)
y = df['cnt']


# Instantiate gb
gb = GradientBoostingRegressor(n_estimators=200, max_depth=4, random_state=2)


# Set seed for reproducibility
SEED = 1

# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

# Fit gb to the training set
gb.fit(X_train, y_train)

# Predict test set labels
y_pred = gb.predict(X_test)

# Compute MSE
mse_test = MSE(y_test, y_pred)

# Compute RMSE
rmse_test = MSE(y_test, y_pred)**(1/2)

# Print RMSE
print('Test set RMSE of gb: {:.3f}'.format(rmse_test))