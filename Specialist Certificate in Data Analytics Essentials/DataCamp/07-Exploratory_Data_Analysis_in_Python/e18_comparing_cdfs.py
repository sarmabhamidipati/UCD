"""
Comparing CDFs

    Evaluate the normal cumulative distribution function using dist.cdf.
    Use the Cdf() function to compute the CDF of log_income.
    Plot the result.

"""
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Cdf
from scipy.stats import norm

gss = pd.read_hdf('gss.hdf5', 'gss')


# Extract realinc and compute its log
log_income = np.log10(gss['realinc'])

# Compute mean and standard deviation
mean, std = log_income.mean(), log_income.std()

# Make a norm object

dist = norm(mean, std)

# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf(log_income).plot()

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()