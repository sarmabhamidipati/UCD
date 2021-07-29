"""
Members vs casual riders over time
Riders can either be "Members", meaning they pay yearly for the ability to take a bike at any time, or
"Casual", meaning they pay at the kiosk attached to the bike dock.
As before, rides has been loaded for you. You're going to use the Pandas method .value_counts(),
which returns the number of instances of each value in a Series. In this case, the counts of "Member" or "Casual".

Instructions
    Set monthly_rides to be a resampled version of rides, by month, based on start date.
    Use the method .value_counts() to find out how many Member and Casual rides there were,
    and divide them by the total number of rides per month.
"""

import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M',on='Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

