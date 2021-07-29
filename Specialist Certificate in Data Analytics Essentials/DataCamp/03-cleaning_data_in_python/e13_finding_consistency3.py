"""
The DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key
questions regarding cleanliness, safety, and satisfaction. Another DataFrame named categories was created,
containing all correct possible values for the survey columns.

In this exercise, you will use both of these DataFrames to find survey answers with inconsistent values,
and drop them, effectively performing an outer and inner join on both these DataFrames as seen in the video exercise.
The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment.

Instructions 3/4

    Create a set out of the cleanliness column in airlines using set() and find the inconsistent category by
    finding the difference in the cleanliness column of categories.
    Find rows of airlines with a cleanliness value not in categories and print the output.

"""

import pandas as pd

categories = pd.read_csv('categories.csv')
airlines = pd.read_csv('airlines.csv')
# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])
print(cat_clean)

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)
print(airlines[cat_clean_rows])

# Print rows with inconsistent category
print(airlines[cat_clean_rows])
