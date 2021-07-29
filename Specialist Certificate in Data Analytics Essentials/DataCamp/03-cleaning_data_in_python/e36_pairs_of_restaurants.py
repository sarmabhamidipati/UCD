"""
in this exercise, you will perform the first step in record linkage and generate possible pairs of rows between
restaurants and restaurants_new. Both DataFrames, pandas and recordlinkage are in your environment.

Instructions

    Instantiate an indexing object by using the Index() function from recordlinkage.
    Block your pairing on cuisine_type by using indexer's' .block() method.
    Generate pairs by indexing restaurants and restaurants_new in that order.
Now that you've generated your pairs, you've achieved the first step of record linkage.
What are the steps remaining to link both restaurants DataFrames, and in what order?
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

"""
Possible Answers

    A.Compare between columns, score the comparison, then link the DataFrames.
    B.Clean the data, compare between columns, link the DataFrames, then score the comparison.
    C.Clean the data, compare between columns, score the comparison, then link the DataFrames.

Answer A
"""
