"""
Plot Income and Education
Here, the GSS dataset has been pre-loaded into a DataFrame called gss.

    Group gss by 'educ'. Store the result in grouped.
    From grouped, extract 'realinc' and compute the mean.
    Plot mean_income_by_educ as a scatter plot. Specify 'o' and alpha=0.5.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf
from scipy.stats import norm
from scipy.stats import linregress
import seaborn as sns
import statsmodels.formula.api as smf


gss = pd.read_hdf('gss.hdf5', 'gss')

# Group by educ
grouped = gss.groupby('educ')

# Compute mean income in each group
mean_income_by_educ = grouped['realinc'].mean()

# Plot mean income as a scatter plot
plt.plot(mean_income_by_educ,'o',alpha=0.5)

# Label the axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.show()