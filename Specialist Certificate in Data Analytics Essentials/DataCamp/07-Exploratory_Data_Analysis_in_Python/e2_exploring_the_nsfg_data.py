"""
Exploring the NSFG data

Calculate the number of rows and columns in the DataFrame nsfg.
Display the names of the columns
Select the column 'birthwgt_oz1' and assign it to a new variable called ounces.
Display the first 5 elements of ounces.
"""
import pandas as pd

nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')
# Display the number of rows and columns
print(nsfg.shape)
# Display the names of the columns
print(nsfg.columns)

# Select column birthwgt_oz1: ounces
ounces = nsfg["birthwgt_oz1"]

# Print the first 5 elements of ounces
print(ounces.head())