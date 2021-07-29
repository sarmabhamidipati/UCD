"""
Now it's finally time to link both DataFrames. You will do so by first extracting all row indices of restaurants_new
that are matching across the columns mentioned above from potential_matches.
Then you will subset restaurants_new on these indices, then append the non-duplicate values to restaurants.
All DataFrames are in your environment, alongside pandas imported as pd.

Instructions

Isolate instances of potential_matches where the row sum is above or equal to 3 by using the .sum() method.
Extract the second column index from matches, which represents row indices of matching record from restaurants_new by
using the .get_level_values() method.
Subset restaurants_new for rows that are not in matching_indices.
Append non_dup to restaurants.

"""

import pandas as pd
import recordlinkage

restaurants = pd.read_csv('restaurant.csv')
restaurants_new = pd.read_csv('restaurant_new.csv')

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)
print(pairs)

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold=0.8)

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
# print(potential_matches)

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
