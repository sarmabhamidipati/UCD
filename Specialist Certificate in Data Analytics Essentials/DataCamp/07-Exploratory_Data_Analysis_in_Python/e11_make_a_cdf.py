"""
Make a CDF

    Select the 'age' column. Store the result in age.
    Compute the CDF of age. Store the result in cdf_age.
    Calculate the CDF of 30.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Cdf

gss = pd.read_hdf('gss.hdf5', 'gss')
# print(gss.head())

# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)

# Calculate the CDF of 30
print(cdf_age[30])

#older than 30
print(cdf_age[cdf_age > cdf_age[30]])
