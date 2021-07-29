"""

In this exercise, you will use both of these DataFrames to find survey answers with inconsistent values, and drop them,
effectively performing an outer and inner join on both these DataFrames as seen in the video exercise.
The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment.

Instructions 4/4

    Print the rows with the consistent categories of cleanliness only.


"""

import pandas as pd

categories = pd.read_csv('categories.csv')
airlines = pd.read_csv('airlines.csv')

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])
