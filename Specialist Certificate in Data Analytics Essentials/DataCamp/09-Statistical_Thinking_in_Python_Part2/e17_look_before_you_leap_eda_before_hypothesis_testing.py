"""
Look before you leap: EDA before hypothesis testing
Instructions

    Use sns.swarmplot() to make a bee swarm plot of the data by specifying the x, y, and data keyword arguments.
    Label your axes.
    Show the plot.

"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('df.csv')

# Make bee swarm plot
_ = sns.swarmplot(df['ID'], df['impact_force'])

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (N)')

# Show the plot
plt.show()
