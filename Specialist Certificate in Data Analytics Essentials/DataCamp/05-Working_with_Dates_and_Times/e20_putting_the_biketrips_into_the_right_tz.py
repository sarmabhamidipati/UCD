"""
Putting the bike trips into the right time zone
Instead of setting the timezones for W20529 by hand, let's assign them to their IANA timezone: 'America/New_York'.
Since we know their political jurisdiction, we don't need to look up their UTC offset. Python will do that for us.

    Import tz from dateutil.
    Assign et to be the timezone 'America/New_York'.
    Within the for loop, set start and end to have et as their timezone (use .replace()).

"""
# Import tz
from dateutil import tz
from datetime import datetime, timedelta, timezone

onebike_datetimes = [
    {'start': datetime(2017, 10, 1, 15, 23, 25), 'end': datetime(2017, 10, 1, 15, 26, 26)},
    {'start': datetime(2017, 10, 1, 15, 42, 57), 'end': datetime(2017, 10, 1, 17, 49, 59)},
    {'start': datetime(2017, 10, 2, 6, 37, 10), 'end': datetime(2017, 10, 2, 6, 42, 53)},
    {'start': datetime(2017, 10, 2, 8, 56, 45), 'end': datetime(2017, 10, 2, 9, 18, 3)},
    {'start': datetime(2017, 10, 2, 18, 23, 48), 'end': datetime(2017, 10, 2, 18, 45, 5)}
]

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=et)
    trip['end'] = trip['end'].replace(tzinfo=et)
