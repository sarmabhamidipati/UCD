"""
Non-linear model of education

    Add a column named 'educ2' to the gss DataFrame; it should contain the values from 'educ' squared.
    Run a regression model that uses 'educ', 'educ2', 'age', and 'age2' to predict 'realinc'.

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


gss = pd.read_hdf('gss.hdf5', 'gss')


# Add a new column with educ squared
gss['educ2'] = gss['educ']**2
gss['age2'] = gss['age']**2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Print the estimated parameters
print(results.params)