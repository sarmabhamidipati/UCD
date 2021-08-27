"""
Income and height
Create a violin plot to plot the distribution of height ('HTM4') in each income ('INCOME2') group.
Specify inner=None to simplify the plot.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf
from scipy.stats import norm
import seaborn as sns
brfss = pd.read_hdf('brfss.hdf5', 'brfss')


# Drop rows with missing data
data = brfss.dropna(subset=['INCOME2', 'HTM4'])

# Make a violin plot
sns.violinplot(x='INCOME2', y='HTM4', data=data, inner=None)


# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Income level')
plt.ylabel('Height in cm')
plt.show()
