"""
Distribution of income
As a first step, you'll compute the mean and standard deviation of the log of incomes using NumPy's np.log10() function.

Then, you'll use the computed mean and standard deviation to make a norm object using the scipy.stats.norm() function.

    Extract 'realinc' from gss and compute its logarithm using np.log10().
    Compute the mean and standard deviation of the result.
    Make a norm object by passing the computed mean and standard deviation to norm().

"""

import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Cdf
from scipy.stats import norm

gss = pd.read_hdf('gss.hdf5', 'gss')


# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = np.mean(income)
std = np.std(income)
print(mean, std)

# Make a norm object

dist = norm(mean,std)

