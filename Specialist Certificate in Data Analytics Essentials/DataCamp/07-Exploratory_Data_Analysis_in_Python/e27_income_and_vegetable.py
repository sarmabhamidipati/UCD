"""
Income and vegetables

    Extract the columns 'INCOME2' and '_VEGESU1' from subset into xs and ys respectively.
    Compute the simple linear regression of these variables.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf
from scipy.stats import norm
from scipy.stats import linregress
import seaborn as sns
brfss = pd.read_hdf('brfss.hdf5', 'brfss')

# Extract the variables
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']

# Compute the linear regression
res = linregress(xs,ys)
print(res)
