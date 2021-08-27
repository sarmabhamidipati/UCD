"""
Creating dummy variables
To do this, you need to binarize it by creating dummy variables, which is what you will do in this exercise.
Instructions
100 XP

    Use the pandas get_dummies() function to create dummy variables from the df DataFrame.
    Store the result as df_region.
    Print the columns of df_region. This has been done for you.
    Use the get_dummies() function again, this time specifying drop_first=True to drop the unneeded dummy
    variable (in this case, 'Region_America').
    Hit 'Submit Answer to print the new columns of df_region and take note of how one column was dropped!

"""
import pandas as pd
import matplotlib.pyplot as plt

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df, drop_first=True)

# Print the new columns of df_region
print(df_region.columns)
