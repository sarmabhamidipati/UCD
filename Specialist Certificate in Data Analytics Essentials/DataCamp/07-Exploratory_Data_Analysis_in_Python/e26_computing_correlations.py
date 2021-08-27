"""
Computing correlations

    From the brfss DataFrame, select the columns 'AGE', 'INCOME2', and '_VEGESU1'.
    Compute the correlation matrix for these variables.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf
from scipy.stats import norm
import seaborn as sns
brfss = pd.read_hdf('brfss.hdf5', 'brfss')


# Select columns
columns = ['AGE', 'INCOME2', '_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())