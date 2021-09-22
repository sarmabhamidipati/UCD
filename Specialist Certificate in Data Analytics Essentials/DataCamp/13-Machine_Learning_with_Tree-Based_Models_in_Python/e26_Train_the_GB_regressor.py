"""
Train the GB regressor
You'll now train the gradient boosting regressor gb that you instantiated in the previous exercise and
predict test set labels.

The dataset is split into 80% train and 20% test. Feature matrices X_train and X_test, as well as the arrays
y_train and y_test are available in your workspace. In addition, we have also loaded the model instance gb
that you defined in the previous exercise.

Instructions
100 XP

    Fit gb to the training set.
    Predict the test set labels and assign the result to y_pred
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

