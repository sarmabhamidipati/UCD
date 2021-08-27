"""
Make a histogram

Plot a histogram of agecon with 20 bins.

Adapt your code to make an unfilled histogram by setting the parameter histtype to be 'step'.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')
agecon = nsfg["agecon"]/100
# Plot the histogram
plt.hist(agecon, bins=20, histtype='step')

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()
