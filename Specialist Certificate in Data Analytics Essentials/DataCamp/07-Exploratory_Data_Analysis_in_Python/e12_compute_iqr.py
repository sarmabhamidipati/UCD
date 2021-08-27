"""
Compute IQR
Calculate the 75th percentile of income and store it in percentile_75th.
Calculate the 25th percentile of income and store it in percentile_25th.
Calculate the interquartile range of income. Store the result in iqr.
"""

import pandas as pd
from empiricaldist import Cdf

gss = pd.read_hdf('gss.hdf5', 'gss')
print(gss.head())

# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)

# Calculate the CDF of 30
#print(cdf_age[30])

#older than 30
#print(cdf_age[cdf_age > cdf_age[30]])

income = gss['realinc']
cdf_income = Cdf(income)
print(cdf_income)
# Calculate the 75th percentile
p=0.75
percentile_75th = cdf_income.inverse(p)
print(percentile_75th)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)