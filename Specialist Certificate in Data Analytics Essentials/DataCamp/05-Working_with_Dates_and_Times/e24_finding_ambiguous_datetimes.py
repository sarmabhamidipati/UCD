"""
The data is loaded as onebike_datetimes, and tz has already been imported from dateutil.
Loop over the trips in onebike_datetimes:

    Print any rides whose start is ambiguous.
    Print any rides whose end is ambiguous.
"""
from datetime import datetime, timedelta, timezone
from dateutil import tz

onebike_datetimes = [{'start': datetime(2017, 10, 1, 15, 23, 25, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime(2017, 10, 1, 15, 26, 26, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime(2017, 10, 1, 15, 42, 57, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime(2017, 10, 1, 17, 49, 59, tzinfo=tz.gettz('US/Eastern'))},
                     {'start': datetime(2017, 10, 2, 6, 37, 10, tzinfo=tz.gettz('US/Eastern')),
                      'end': datetime(2017, 10, 2, 6, 42, 53, tzinfo=tz.gettz('US/Eastern'))}
                     ]

# Loop over trips
for trip in onebike_datetimes:
    # Rides with ambiguous start
    if tz.datetime_ambiguous(trip['start']):
        print("Ambiguous start at " + str(trip['start']))
    # Rides with ambiguous end
    if tz.datetime_ambiguous(trip['end']):
        print("Ambiguous end at " + str(trip['end']))
