"""
Writing an iterator to load data in chunks (3)
The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use.
Instructions
100 XP

    Write a list comprehension to generate a list of values from pops_list for the new column 'Total Urban Population'.
    The output expression should be the product of the first and second element in each tuple in pops_list.
    Because the 2nd element is a percentage, you also need to either multiply the result by 0.01 or divide it by 100.
    In addition, note that the column 'Total Urban Population' should only be able to take on integer values.
    To ensure this, make sure you cast the output expression to an integer with int().
    Create a scatter plot where the x-axis are values from the 'Year' column and
    the y-axis are values from the 'Total Urban Population' column.

"""
import pandas as pd
import matplotlib.pyplot as plt

# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'],
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)
print(pops_list)
# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
