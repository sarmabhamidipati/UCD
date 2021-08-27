"""
EDA of beak depths of Darwin's finches

    Create the beeswarm plot.
    Label the axes.
    Show the plot.

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('df1.csv')

# Create bee swarm plot
_ = sns.swarmplot(x=df['year'], y=df['beak_depth'], data=df)

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

# Show the plot
plt.show()
