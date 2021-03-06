"""
Clean a variable
f you use .value_counts() to view the responses, you'll see that the value 8 appears once, and if you consult the
codebook, you'll see that this value indicates that the respondent refused to answer the question.

Your job in this exercise is to replace this value with np.nan.
Recall from the video how Allen replaced the values 98 and 99 in the ounces column using the .replace() method:

ounces.replace([98, 99], np.nan, inplace=True)


    In the 'nbrnaliv' column, replace the value 8, in place, with the special value NaN.
    Confirm that the value 8 no longer appears in this column by printing the values and their frequencies.

"""
import pandas as pd
import numpy as np

pd.options.display.max_columns=None

nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')

print(nsfg['nbrnaliv'].value_counts())

# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())

print(nsfg[nsfg['nbrnaliv'].isna()])

print(nsfg[nsfg['nbrnaliv'].isna()])