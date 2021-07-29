"""
Timezones in Pandas
Instructions 1/2

Make the Start date column timezone aware by localizing it to 'America/New_York' while ignoring any ambiguous datetimes.
Now switch the Start date column to the timezone 'Europe/London' using the .dt.tz_convert() method.
dt.tzconvert() converts to a new timezone, whereas dt.tzlocalize() sets a timezone in the first place.
"""
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York',ambiguous='NaT')

# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
print(rides['Start date'].iloc[0])