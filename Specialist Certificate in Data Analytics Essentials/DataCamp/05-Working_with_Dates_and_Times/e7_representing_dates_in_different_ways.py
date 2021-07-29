"""
Representing dates in different ways
Let's try printing out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida),
in a number of different ways, to practice using the .strftime() method.

A date object called andrew has already been created
Print andrew in the format 'MONTH (YYYY)', using %B for the month's full name, which in this case will be August.
Print andrew in the format 'YYYY-DDD' (where DDD is the day of the year) using %j.
"""
# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime("%Y-%m"))

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime("%B (%Y)"))

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime("%Y-%j"))