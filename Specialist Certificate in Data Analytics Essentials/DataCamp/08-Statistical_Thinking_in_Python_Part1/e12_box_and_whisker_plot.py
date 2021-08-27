"""
Box-and-whisker plot

    The set-up is exactly the same as for the bee swarm plot; you just call sns.boxplot()
    with the same keyword arguments as you would sns.swarmplot(). The x-axis is 'species' and y-axis is 'petal length (cm)'.
    Don't forget to label your axes!
    Display the figure using the normal call.

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('df.csv')

# Create box plot with Seaborn's default settings

_ = sns.boxplot(x='species', y='petal length (cm)', data=df)
# Label the axes

_ = plt.xlabel('species')
_ = plt.ylabel('petal length')

# Show the plot

plt.show()
