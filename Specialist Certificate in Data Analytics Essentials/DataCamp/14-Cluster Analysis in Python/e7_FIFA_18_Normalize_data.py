"""
FIFA 18: Normalize data
You will explore various features of the data as we move ahead in the course. In this exercise,
you will work with two columns, eur_wage, the wage of a player in Euros and eur_value, their current transfer market value.

The data for this exercise is stored in a Pandas dataframe, fifa. whiten from scipy.cluster.vq
and matplotlib.pyplot as plt have been pre-loaded.

Instructions 1/3
50 XP

    Scale the values of eur_wage and eur_value using the whiten() function.
    Plot the scaled wages and transfer values of players using the .plot() method of Pandas.
    Check the mean and standard deviation of the scaled data using the .describe() method of Pandas.

"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten

fifa = pd.read_csv('fifa_18_sample_data.csv')

# print(fifa.head(10))

# Scale wage and value
fifa['scaled_wage'] = whiten(fifa['eur_wage'])
fifa['scaled_value'] = whiten(fifa['eur_value'])

# Plot the two columns in a scatter plot
fifa.plot(x='scaled_wage', y='scaled_value', kind='scatter')
plt.show()

# Check mean and standard deviation of scaled values
print(fifa[['scaled_wage', 'scaled_value']].describe())
