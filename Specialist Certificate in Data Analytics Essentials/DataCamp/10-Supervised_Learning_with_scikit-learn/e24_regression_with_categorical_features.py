"""
Regression with categorical features
Having created the dummy variables from the 'Region' feature, you can build regression models as you did before.
Here, you'll use ridge regression to perform 5-fold cross-validation.

The feature array X and target variable array y have been pre-loaded.
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score


# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gapminder.csv')


# convert dataframe column to numpy array
X = df['fertility'].to_numpy()
y = df['life'].to_numpy()
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X, y, cv=5)

# Print the cross-validated scores
print(ridge_cv)
