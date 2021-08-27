"""
The BRFSS dataset includes a variable, 'AGE' (note the capitalization!), which represents each respondent's age.
To protect respondents' privacy, ages are rounded off into 5-year bins. 'AGE' contains the midpoint of the bins.


    Extract the variable 'AGE' from the DataFrame brfss and assign it to age.
    Get the PMF of age and plot it as a bar chart.
"""

import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf
from scipy.stats import norm
import seaborn as sns

brfss = pd.read_hdf('brfss.hdf5', 'brfss')
# Select the first 1000 respondents
brfss = brfss[:1000]


# Extract age
age = brfss['AGE']

# Plot the PMF
pmf_age = Pmf(age)
pmf_age.bar()

# Label the axes
plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()