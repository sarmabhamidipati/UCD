"""
Jittering

    Add random noise to age with mean 0 and standard deviation 2.5.
    Make a scatter plot between weight and age with marker size 5 and alpha=0.2. Be sure to also specify 'o'.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf
from scipy.stats import norm
import seaborn as sns

brfss = pd.read_hdf('brfss.hdf5', 'brfss')
# Select the first 1000 respondents
brfss = brfss[:1000]

# Extract age and weight
# Add jittering to age
age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', alpha=0.2)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')

plt.show()
