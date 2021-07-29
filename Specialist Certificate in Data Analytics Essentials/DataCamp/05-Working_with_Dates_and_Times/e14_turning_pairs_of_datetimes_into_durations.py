"""
Turning pairs of datetimes into durations
Continuing our work from a previous coding exercise, the bike trip data has been loaded as the list onebike_datetimes.
Each element of the list consists of two datetime objects, corresponding to the start and end of a trip, respectively.
Within the loop:

    Use arithmetic on the start and end elements to find the length of the trip
    Save the results to trip_duration.
    Calculate trip_length_seconds from trip_duration.
"""
from datetime import datetime
from datetime import timedelta

onebike_datetimes = [
    {'start': datetime(2017, 10, 1, 15, 23, 25), 'end': datetime(2017, 10, 1, 15, 26, 26)},
    {'start': datetime(2017, 10, 1, 15, 42, 57), 'end': datetime(2017, 10, 1, 17, 49, 59)},
    {'start': datetime(2017, 10, 2, 6, 37, 10), 'end': datetime(2017, 10, 2, 6, 42, 53)},
    {'start': datetime(2017, 10, 2, 8, 56, 45), 'end': datetime(2017, 10, 2, 9, 18, 3)}]

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
    #print(trip)
    # Create a timedelta object corresponding to the length of the trip

    trip_duration = trip['end'] - trip['start']
    print(trip_duration)
    # Get the total elapsed seconds in trip_duration
    trip_length_seconds = trip_duration.total_seconds()

    # Append the results to our list
    onebike_durations.append(trip_length_seconds)

