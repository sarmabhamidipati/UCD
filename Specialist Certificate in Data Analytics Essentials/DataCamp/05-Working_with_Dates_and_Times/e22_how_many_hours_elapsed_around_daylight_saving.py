"""
How many hours elapsed around daylight saving?
Let's look at March 12, 2017, in the Eastern United States, when Daylight Saving kicked in at 2 AM.

If you create a datetime for midnight that night, and add 6 hours to it, how much time will have elapsed?
You already have a datetime called start, set for March 12, 2017 at midnight, set to the timezone 'America/New_York'.
Add six hours to start and assign it to end. Look at the UTC offset for the two results.

You added 6 hours, and got 6 AM, despite the fact that the clocks springing forward means only 5 hours
would have actually elapsed!
Calculate the time between start and end. How much time does Python think has elapsed?
Move your datetime objects into UTC and calculate the elapsed time again.
Once you're in UTC, what result do you get?
"""
# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo=tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds() / (60 * 60))

# What if we move to UTC?
print((end.astimezone(timezone.utc) - start.astimezone(timezone.utc)) \
      .total_seconds() / (60 * 60))
