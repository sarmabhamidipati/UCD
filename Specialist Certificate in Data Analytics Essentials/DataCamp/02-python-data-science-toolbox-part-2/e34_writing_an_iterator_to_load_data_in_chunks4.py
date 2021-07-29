"""
Writing an iterator to load data in chunks (4)
You're going to use the data from 'ind_pop_data.csv', available in your current directory.
The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use.

Instructions
100 XP

    Initialize an empty DataFrame data using pd.DataFrame().
    In the for loop, iterate over urb_pop_reader to be able to process all the DataFrame chunks in the dataset.
    Using the method append() of the DataFrame data, append df_pop_ceb to data.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:
    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
               df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
