"""
Plot income CDFs
Fill in the missing lines of code to plot the CDFs.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Cdf

gss = pd.read_hdf('gss.hdf5', 'gss')
#print(gss.head())

# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school (12 or fewer years of education)
high = (educ <= 12)
#print(high.mean())

income = gss['realinc']

# Plot the CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()