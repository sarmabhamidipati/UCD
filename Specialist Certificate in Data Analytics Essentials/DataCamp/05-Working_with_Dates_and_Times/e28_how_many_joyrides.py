"""
How many joyrides
Suppose you have a theory that some people take long bike rides before putting their bike back in the same dock.
Let's call these rides "joyrides".
Instructions

    Create a Pandas Series which is True when Start station and End station are the same,
    and assign the result to joyrides.
    Calculate the median duration of all rides.
    Calculate the median duration of joyrides.

"""
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds".format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds".format(rides[joyrides]['Duration'].median()))
