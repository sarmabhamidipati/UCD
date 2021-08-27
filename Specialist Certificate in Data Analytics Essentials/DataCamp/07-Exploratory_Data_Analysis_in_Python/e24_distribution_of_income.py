"""
Distrbution of Income

    Extract 'INCOME2' from the brfss DataFrame and assign it to income.
    Plot the PMF of income as a bar chart.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf
from scipy.stats import norm
import seaborn as sns
brfss = pd.read_hdf('brfss.hdf5', 'brfss')

# Extract income
income = brfss['INCOME2']
income = income[:10000]

# Plot the PMF
Pmf(income).bar()


# Label the axes
plt.xlabel('Income level')
plt.ylabel('PMF')
plt.show()