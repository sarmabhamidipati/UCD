"""
Instantiate the model
In the following set of exercises, you'll diagnose the bias and variance problems of a regression tree.
The regression tree you'll define in this exercise will be used to predict the mpg consumption of cars
from the auto dataset using all available features.

We have already processed the data and loaded the features matrix X and the array y in your workspace.
In addition, the DecisionTreeRegressor class was imported from sklearn.tree.
"""

import pandas as pd
# Import train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


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
