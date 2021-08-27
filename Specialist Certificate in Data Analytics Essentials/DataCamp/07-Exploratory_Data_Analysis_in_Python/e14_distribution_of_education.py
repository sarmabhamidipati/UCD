"""
Distribution of Education

What fraction of respondents report that they have 12 years of education or fewer?
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Cdf

gss = pd.read_hdf('gss.hdf5', 'gss')
#print(gss.head())

# Select realinc
educ = gss['educ']

# Make the CDF
cdf_educ = Cdf(educ)

print(cdf_educ[cdf_educ < 12].value_counts())