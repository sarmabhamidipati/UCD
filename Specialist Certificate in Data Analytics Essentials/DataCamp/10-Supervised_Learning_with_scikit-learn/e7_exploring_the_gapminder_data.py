"""
Exploring the Gapminder data

As always, it is important to explore your data before building models. On the right, we have constructed a heatmap
showing the correlation between the different features of the Gapminder dataset, which has been pre-loaded into a
DataFrame as df and is available for exploration in the IPython Shell. Cells that are in green show positive
correlation, while cells that are in red show negative correlation. Take a moment to explore this: Which
features are positively correlated with life, and which ones are negatively correlated? Does this match your intuition?

Then, in the IPython Shell, explore the DataFrame using pandas methods such as .info(), .describe(), .head().

In case you are curious, the heatmap was generated using Seaborn's heatmap function and the following line of code,
where df.corr() computes the pairwise correlation between columns:

sns.heatmap(df.corr(), square=True, cmap='RdYlGn')

Once you have a feel for the data, consider the statements below and select the one that is not true. After this,
Hugo will explain the mechanics of linear regression in the next video and you will be on your
way building regression models!
"""

# Import numpy and pandas
import numpy as np
import pandas as pd

# Read the CSV file into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create arrays for features and target variable
y = df['life']
X = df['fertility']

# Print the dimensions of y and X before reshaping
print("Dimensions of y before reshaping: ", y.shape)
print("Dimensions of X before reshaping: ", X.shape)

# Reshape X and y
y_reshaped = y.values.reshape(-1, 1)
X_reshaped = X.values.reshape(-1, 1)

# Print the dimensions of y_reshaped and X_reshaped
print("Dimensions of y after reshaping: ", y_reshaped.shape)
print("Dimensions of X after reshaping: ", X_reshaped.shape)



print(df.dtypes)
print(df.info())
print(df.describe())

print(type(X))