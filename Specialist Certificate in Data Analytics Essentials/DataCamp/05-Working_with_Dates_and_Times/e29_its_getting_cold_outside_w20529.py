"""
It's getting cold outside, W20529
How might the weather or the season have affected the length of bike trips?

    Resample rides to the daily level, based on the Start date column.
    Plot the .size() of each result.
Since the daily time series is so noisy for this one bike, change the resampling to be monthly.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Resample rides to daily, take the size, plot the results
rides.resample('D', on='Start date').size().plot(ylim=[0, 15])

# Show the results
plt.show()

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='Start date').size().plot(ylim=[0, 150])

# Show the results
plt.show()