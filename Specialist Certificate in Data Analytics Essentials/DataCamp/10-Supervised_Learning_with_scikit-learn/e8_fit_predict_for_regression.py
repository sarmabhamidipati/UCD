"""
Fit & predict for regression
Now, you will fit a linear regression and predict life expectancy using just one feature. You saw Andy do this earlier
using the 'RM' feature of the Boston housing dataset. In this exercise, you will use the 'fertility' feature
of the Gapminder dataset. Since the goal is to predict life expectancy, the target variable here is 'life'.
The array for the target variable has been pre-loaded as y and the array for 'fertility'
has been pre-loaded as X_fertility.

A scatter plot with 'fertility' on the x-axis and 'life' on the y-axis has been generated.
As you can see, there is a strongly negative correlation, so a linear regression should be able to
capture this trend. Your job is to fit a linear regression and then predict the life expectancy,
overlaying these predicted values on the plot to generate a regression line. You will also compute and print the
R ^ 2 score using scikit-learn's .score() method.
"""
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
# Import LinearRegression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# convert dataframe column to numpy array
X_fertility = df['fertility'].to_numpy()
y = df['life'].to_numpy()
X_fertility = X_fertility.reshape(-1, 1)
y = y.reshape(-1, 1)
# print(X_fertility.shape, X_fertility.ndim)
# print(y.shape, y.ndim)


# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1, 1)

# Fit the model to the data
reg.fit(X_fertility, y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2
print(reg.score(X_fertility, y))

# Plot regression line
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
