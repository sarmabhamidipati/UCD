"""
Compute a variable

For each pregnancy in the NSFG dataset, the variable 'agecon' encodes the respondent's
age at conception, and 'agepreg' the respondent's age at the end of the pregnancy.

Both variables are recorded as integers with two implicit decimal places, so the value 2575 means that the respondent's age was 25.75.

Select 'agecon' and 'agepreg', divide them by 100, and assign them to the local variables agecon and agepreg.

Compute the difference, which is an estimate of the duration of the pregnancy.
Keep in mind that for each pregnancy, agepreg will be larger than agecon.
"""

import pandas as pd
import numpy as np

pd.options.display.max_columns=None

nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')

# Select the columns and divide by 100
agecon = nsfg["agecon"]/100
agepreg = nsfg["agepreg"]/100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())