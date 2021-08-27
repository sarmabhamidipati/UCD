"""
Dropping missing data
In this exercise, your job is to convert the '?'s to NaNs, and then drop the rows that contain them from the DataFrame.

    Explore the DataFrame df in the IPython Shell. Notice how the missing value is represented.
    Convert all '?' data points to np.nan.
    Count the total number of NaNs using the .isnull() and .sum() methods. This has been done for you.
    Drop the rows with missing values from df using .dropna().
    Hit 'Submit Answer' to see how many rows were lost by dropping the missing values.

"""
import pandas as pd
import numpy as np
df = pd.read_csv('voting.csv')

# Convert '?' to NaN
df[df == '?'] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape of new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))
