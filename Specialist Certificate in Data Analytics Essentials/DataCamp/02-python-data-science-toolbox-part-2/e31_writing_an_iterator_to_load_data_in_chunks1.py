"""
Writing an iterator to load data in chunks (1)
In this exercise, you will read a file in small DataFrame chunks with read_csv().
 You're going to use the World Bank Indicators data 'ind_pop.csv', available in your current directory,
 to look at the urban population indicator for numerous countries and years.
 Instructions
100 XP

    Use pd.read_csv() to read in 'ind_pop.csv' in chunks of size 10. Assign the result to df_reader.
    Print the first two chunks from df_reader.

"""

# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))
