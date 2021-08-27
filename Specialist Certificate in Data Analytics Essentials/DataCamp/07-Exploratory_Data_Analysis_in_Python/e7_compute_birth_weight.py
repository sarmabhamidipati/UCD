"""
Compute birth weight

    Make a Boolean Series called full_term that is true for babies with 'prglngth' greater than or equal to 37 weeks.
    Use full_term and birth_weight to select birth weight in pounds for full-term babies.
    Store the result in full_term_weight.
    Compute the mean weight of full-term babies.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')
agecon = nsfg["agecon"]/100
# Plot the histogram
plt.hist(agecon, bins=20, histtype='step')

# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth'] >= 37

# Select the weights of full-term babies
full_term_weight = birth_weight[full_term]

# Compute the mean weight of full-term babies
print(full_term_weight.mean())