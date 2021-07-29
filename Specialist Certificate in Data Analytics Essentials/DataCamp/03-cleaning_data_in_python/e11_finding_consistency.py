"""
Finding consistency
In this exercise, you will use both of these DataFrames to find survey answers with inconsistent values,
and drop them, effectively performing an outer and inner join on both these DataFrames as seen in the video exercise.
The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment.
Instructions 1/4

    Print the categories DataFrame and take a close look at all possible correct categories of the survey columns.
    Print the unique values of the survey columns in airlines using the .unique() method.

"""

import pandas as pd
categories = pd.read_csv('categories.csv')
airlines = pd.read_csv('airlines.csv')
# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Cleanliness: ', airlines['safety'].unique(), "\n")
print('Cleanliness: ', airlines['satisfcation'].unique(), "\n")