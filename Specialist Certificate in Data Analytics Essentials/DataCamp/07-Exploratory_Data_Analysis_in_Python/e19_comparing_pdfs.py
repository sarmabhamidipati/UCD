"""
Comparing PDFs


    Evaluate the normal PDF using dist, which is a norm object with the same mean and standard deviation as the data.
    Make a KDE plot of the logarithms of the incomes, using log_income, which is a Series object.

"""
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Cdf
from scipy.stats import norm
import seaborn as sns

gss = pd.read_hdf('gss.hdf5', 'gss')


# Extract realinc and compute its log
log_income = np.log10(gss['realinc'])

# Compute mean and standard deviation
mean, std = log_income.mean(), log_income.std()

# Make a norm object

dist = norm(mean, std)

# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)


# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)


# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()