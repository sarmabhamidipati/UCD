"""
The restaurants DataFrame is in your environment, and you have access to a categories list
containing the correct cuisine types ('italian', 'asian', and 'american').
Instructions
1. Return all of the unique values in the cuisine_type column of restaurants.
2. As a first step, create a list of matches, comparing 'italian' with the restaurant types listed
   in the cuisine_type column.
3.
    Within the for loop, use an if statement to check whether the similarity score in each match is
    greater than or equal to 80.
    If it is, use .loc to select rows where cuisine_type in restaurants is equal to
    the current match (which is the first element of match), and reassign them to be 'italian'.

4.

Finally, you'll adapt your code to work with every restaurant type in categories.

    Using the variable cuisine to iterate through categories, embed your code from the previous step in an outer
    for loop. Inspect the final result. This has been done for you.


"""
from fuzzywuzzy import process
import pandas as pd

categories = ['italian', 'asian', 'american']
restaurants = pd.read_csv('restaurant.csv')

# Inspect the unique values of the cuisine_type column
print(restaurants['cuisine_type'].unique())

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Inspect the first 5 matches
print(matches[0:5])

# Iterate through the list of matches to italian
for match in matches:
    #print(match[1])
    # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
        # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
        restaurants.loc[restaurants['cuisine_type'] == match[0], 'cuisine_type'] = 'italian'
# Iterate through categories
for cuisine in categories:
    # Create a list of matches, comparing cuisine with the cuisine_type column
    matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

    # Iterate through the list of matches
    for match in matches:
        # Check whether the similarity score is greater than or equal to 80
        if match[1] >= 80:
            # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
            restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine

# Inspect the final result
print(restaurants['cuisine_type'].unique())