"""
onebike_datetimes is already loaded and in the right timezone.
tz and timezone have been imported. Use tz.UTC for the timezone.

    Complete the if statement to be true only when a ride's start comes after its end.
    When start is after end, call tz.enfold() on the end so you know it refers to the one
    after the daylight savings time change.
    After the if statement, convert the start and end to UTC so you can make a proper comparison.

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

trip_durations = []
for trip in onebike_datetimes:
    # When the start is later than the end, set the fold to be 1
    if trip['start'] > trip['end']:
        trip['end'] = tz.enfold(trip['end'])
    # Convert to UTC
    start = trip['start'].astimezone(tz.UTC)
    end = trip['end'].astimezone(tz.UTC)

    # Subtract the difference
    trip_length_seconds = (end - start).total_seconds()
    trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))
