"""
Counting events before and after noon
Each element of the list is a dictionary with two entries: start is a datetime object corresponding to the start of
a trip (when a bike is removed from the dock) and end is a datetime object corresponding to the end of a trip
(when a bike is put back into a dock).

    Within the for loop, complete the if statement to check if the trip started before noon.
    Within the for loop, increment trip_counts['AM'] if the trip started before noon, and trip_counts['PM'] if it started after noon.

"""
from datetime import  datetime
import pandas as pd

onebike_datetimes_df = pd.read_csv("capital-onebike.csv")

# convert dataframe to a list of dictionaries
#onebike_datetimes = onebike_datetimes_df[["Start date", "End date"]].to_dict('records')
#print(onebike_datetimes)
onebike_datetimes = [
 {'start': datetime(2017, 10, 1, 15, 23, 25), 'end': datetime(2017, 10, 1, 15, 26, 26)},
 {'start': datetime(2017, 10, 1, 15, 42, 57), 'end': datetime(2017, 10, 1, 17, 49, 59)},
 {'start': datetime(2017, 10, 2, 6, 37, 10), 'end': datetime(2017, 10, 2, 6, 42, 53)},
 {'start': datetime(2017, 10, 2, 8, 56, 45), 'end': datetime(2017, 10, 2, 9, 18, 3)},
 {'start': datetime(2017, 10, 2, 18, 23, 48), 'end': datetime(2017, 10, 2, 18, 45, 5)},
 {'start': datetime(2017, 10, 2, 18, 48, 8), 'end': datetime(2017, 10, 2, 19, 10, 54)},
 {'start': datetime(2017, 10, 2, 19, 18, 10), 'end': datetime(2017, 10, 2, 19, 31, 45)},
 {'start': datetime(2017, 10, 2, 19, 37, 32), 'end': datetime(2017, 10, 2, 19, 46, 37)}
]

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
for trip in onebike_datetimes:
    # Check to see if the trip starts before noon
    if trip['start'].hour < 12:
        # Increment the counter for before noon
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon
        trip_counts['PM'] += 1

print(trip_counts)