"""
Using StatsModels

    Compute the regression of '_VEGESU1' as a function of 'INCOME2' using SciPy's linregress().
    Compute the regression of '_VEGESU1' as a function of 'INCOME2' using StatsModels' smf.ols().

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


brfss = pd.read_hdf('brfss.hdf5', 'brfss')


# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs,ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data=brfss).fit()
print(results.params)