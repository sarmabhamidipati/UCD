"""
Loading a csv file in Pandas

The capital_onebike.csv file covers the October, November and December rides of the Capital Bikeshare bike W20529.

    Import Pandas.
    Complete the call to read_csv() so that it correctly parses the date columns Start date and End date.

"""

# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])
print(rides.dtypes)