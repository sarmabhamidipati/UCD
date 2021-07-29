"""
Instructions 1/2

    Import process from fuzzywuzzy.
    Store the unique cuisine_types into unique_types.
    Calculate the similarity of 'asian', 'american', and 'italian' to all possible cuisine_types
    using process.extract(), while returning all possible matches.

"""
# Import process from fuzzywuzzy
from fuzzywuzzy import  process
import pandas as pd
restaurants = pd.read_csv('restaurant.csv')

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))