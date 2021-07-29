"""
On time
Two dictionaries, east and west, both with the keys date and price, have already been loaded.
You can use print() to view them in the IPython Shell.

Inside the f-string, access the values of the keys price and date in east dictionary. Format the date to month-day-year.

Inside the f-string, access the values of the keys price and date in west dictionary. Format the date to month-day-year.
"""
from datetime import datetime

east = {'date': datetime(2007, 4, 20, 0, 0), 'price': 1232443}
west = {'date': datetime(2006, 5, 26, 0, 0), 'price': 1432673}

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")
# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}")