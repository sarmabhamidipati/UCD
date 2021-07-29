"""
The long and the short of why time is hard
As before, data has been loaded as onebike_durations.

    Calculate shortest_trip from onebike_durations.
    Calculate longest_trip from onebike_durations.
    Print the results, turning shortest_trip and longest_trip into strings so they can print.

"""
from datetime import datetime, timedelta


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

# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)
print(total_elapsed_time)

# What was the total number of trips?
number_of_trips = len(onebike_durations)
print(number_of_trips)
# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)

# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

# Print out the results
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")