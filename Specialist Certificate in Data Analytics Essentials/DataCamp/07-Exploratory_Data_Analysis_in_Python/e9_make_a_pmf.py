"""
Make a PMF

Make a PMF for year with normalize=False and display the result.
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf

gss = pd.read_hdf('gss.hdf5', 'gss')
print(gss.head())

year = gss['year']
print(type(year))
# Compute the PMF for year
pmf_year = Pmf.from_seq(year, normalize=False)

# Print the result
print(pmf_year)
