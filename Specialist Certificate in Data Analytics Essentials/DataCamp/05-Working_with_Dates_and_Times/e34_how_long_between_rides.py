"""
How long between rides?
For your final exercise, let's take advantage of Pandas indexing to do something interesting.
How much time elapsed between rides?

Instructions
    Calculate the difference in the Start date of the current row and the End date of the previous row
    and assign it to rides['Time since'].
    Convert rides['Time since'] to seconds to make it easier to work with.
    Resample rides to be in monthly buckets according to the Start date.
    Divide the average by (60*60) to get the number of hours on average that W20529
    waited in the dock before being picked up again.
"""
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']
# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on='Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean() / (60 * 60))
