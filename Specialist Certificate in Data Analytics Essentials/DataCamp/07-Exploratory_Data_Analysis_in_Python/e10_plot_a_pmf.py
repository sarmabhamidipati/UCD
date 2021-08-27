"""
Plot a PMF
Select the 'age' column from the gss DataFrame and store the result in age.
Make a normalized PMF of age. Store the result in pmf_age.
Plot pmf_age as a bar chart.
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Pmf

gss = pd.read_hdf('gss.hdf5', 'gss')
print(gss.head())

age = gss['age']
print(type(age))
# Compute the PMF for year
pmf_age = Pmf.from_seq(age, normalize=False)

# Print the result
print(pmf_age)

# Plot the PMF
pmf_age.bar(label='age')
pmf_age.plot()
# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()
