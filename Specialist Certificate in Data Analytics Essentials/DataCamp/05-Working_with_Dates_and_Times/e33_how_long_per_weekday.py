"""
How long per weekday?
Pandas has a number of datetime-related attributes within the .dt accessor.
Many of them are ones you've encountered before, like .dt.month.
Others are convenient and save time compared to standard Python, like .dt.weekday_name.

    Add a new column to rides called 'Ride start weekday', which is the weekday of the Start date.
    Print the median ride duration for each weekday.

"""
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']
# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.day_name()


# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())
