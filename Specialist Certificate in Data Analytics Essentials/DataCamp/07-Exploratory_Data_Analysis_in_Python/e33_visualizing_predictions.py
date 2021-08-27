"""
Visualizing predictions
Now let's visualize the results from the previous exercise!

    Plot mean_income_by_educ using circles ('o'). Specify an alpha of 0.5.
    Plot the prediction results with a line, with df['educ'] on the x-axis and pred on the y-axis.

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
gss['educ2'] = gss['educ'] ** 2
gss['age2'] = gss['age'] ** 2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0, 20)
df['age'] = 30
df['educ2'] = df['educ'] ** 2
df['age2'] = df['age'] ** 2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())
# Plot mean income in each age group
plt.clf()
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ, 'o', alpha=0.5)

# Plot the predictions
pred = results.predict(df)
plt.plot(df['educ'], pred, label='Age 30')

# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()