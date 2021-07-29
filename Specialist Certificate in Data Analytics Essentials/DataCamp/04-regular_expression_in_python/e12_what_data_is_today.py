"""
What day is today?

    Import the function datetime from the module datetime .
    Obtain the date of today and assign it to the variable get_date.
    Complete the string message by adding to the placeholders named today and the format specifiers to
    format the date as month_name day, year and time as hour:minutes.
    Print the message using the .format() method and the variable get_date to replace the named placeholders.

"""
# Import datetime
from datetime import datetime

# Assign date to get_date
get_date = datetime.today()

# Add named placeholders with format specifiers
name = ":%B %d %Y :%H:%M"

message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date))
