"""
Regularization I: Lasso
In the video, you saw how Lasso selected out the 'RM' feature as being the most important for predicting
Boston house prices, while shrinking the coefficients of certain other features to 0. Its ability to perform
feature selection in this way becomes even more useful when you are dealing with data involving thousands of features.

In this exercise, you will fit a lasso regression to the Gapminder data you have been working with and
plot the coefficients. Just as with the Boston data, you will find that the coefficients of
some features are shrunk to 0, with only the most important ones remaining.

The feature and target variable arrays have been pre-loaded as X and y.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Lasso

gapminder = pd.read_csv('gapminder.csv')
gapminder1 = gapminder[['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP', 'BMI_female', 'child_mortality']]
df_columns = gapminder1.columns

X = gapminder.drop('life', axis=1).values

y = gapminder['life'].values

print(df_columns)
print(X[0])
print("Dimension of Array is ", X.ndim)
print("Shape of the Array is ", X.shape)
print("Size of the  array is ", X.size)

print(y[0])
print("Dimension of Array is ", y.ndim)
print("Shape of the Array is ", y.shape)
print("Size of the  array is ", y.size)

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4, normalize=True)

# Fit the regressor to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.fit(X, y).coef_
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
