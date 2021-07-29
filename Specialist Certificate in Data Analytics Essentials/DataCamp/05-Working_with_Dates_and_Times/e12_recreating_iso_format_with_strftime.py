"""
Recreating ISO format with strftime()
Re-create the .isoformat() method, using .strftime(), and print the first trip start in our data set.

    Complete fmt to match the format of ISO 8601.
    Print first_start with both .isoformat() and .strftime(); they should match.

"""
from datetime import datetime
onebike_datetime_strings = [('2017-10-01 15:23:25', '2017-10-01 15:26:26'),
                            ('2017-10-01 15:42:57', '2017-10-01 17:49:59'),
                            ('2017-10-02 06:37:10', '2017-10-02 06:42:53'),
                            ('2017-10-02 08:56:45', '2017-10-02 09:18:03'),
                            ('2017-10-02 18:23:48', '2017-10-02 18:45:05'),
                            ('2017-10-02 18:48:08', '2017-10-02 19:10:54'),
                            ('2017-10-02 19:18:10', '2017-10-02 19:31:45')
                            ]
# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
    trip = {'start': datetime.strptime(start, fmt),
            'end': datetime.strptime(end, fmt)}

    # Append the trip
    onebike_datetimes.append(trip)
#print(onebike_datetimes)
# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))
