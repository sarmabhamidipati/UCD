"""
Combining groupby() and resample()
 For example, rides.groupby('Member type').size() would tell us how many rides there were by member type in
 our entire DataFrame.

.resample() can be called after .groupby(). For example, how long was the median ride by month, and by Membership type?
Instructions
100 XP

    Complete the .groupby() call to group by 'Member type', and the .resample() call to resample according
    to 'Start date', by month.
    Print the median Duration for each group.

"""
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])
# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']
# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type').resample('M', on='Start date')

# Print the median duration for each group
print(grouped['Duration'].median())
