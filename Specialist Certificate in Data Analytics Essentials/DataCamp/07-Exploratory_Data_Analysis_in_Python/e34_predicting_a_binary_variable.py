"""
Predicting a binary variable
In the GSS dataset, the variable grass records the answer to the question
"Do you think the use of marijuana should be made legal or not?"

Fill in the parameters of smf.logit() to predict grass using the variables age, age2, educ, and educ2,
along with sex as a categorical variable.
Add a column called educ and set it to 12 years; then compute a second column, educ2, which is the square of educ.
Generate separate predictions for men and women.
Fill in the missing code to compute the mean of 'grass' for each age group,
and then the arguments of plt.plot() to plot pred2 versus df['age'] with the label 'Female'.
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


# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
formula = 'grass ~ age + age2 + educ + educ2 + C(sex)'
results = smf.ols(formula, data=gss).fit()

print(results.params)

# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ'] **2

# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

plt.clf()
grouped = gss.groupby('age')
favor_by_age = grouped.mean()
plt.plot(favor_by_age, 'o', alpha=0.5)

plt.plot(df['age'], pred1, label='Male')
plt.plot(df['age'], pred2, label='Female')

plt.xlabel('Age')
plt.ylabel('Probability of favoring legalization')
plt.legend()
plt.show()