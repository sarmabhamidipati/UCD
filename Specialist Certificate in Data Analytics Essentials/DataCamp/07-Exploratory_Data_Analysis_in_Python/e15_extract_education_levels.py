"""
Extract education levels

    Complete the line that identifies respondents with associate degrees, that is, people with 14 or more
    years of education but less than 16.
    Complete the line that identifies respondents with 12 or fewer years of education.
    Confirm that the mean of high is the fraction we computed in the previous exercise, about 53%.

"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from empiricaldist import Cdf

gss = pd.read_hdf('gss.hdf5', 'gss')
#print(gss.head())

# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school (12 or fewer years of education)
high = (educ <= 12)
print(high.mean())