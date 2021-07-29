"""
Flying home
The variable flight containing one email subject was loaded in your session. You can use print() to view it in the IPython Shell.
Import the re module.
Complete the regular expression to match and capture all the flight information required.
Only the first parenthesis were placed for you.
Find all the matches corresponding to each piece of information about the flight. Assign it to flight_matches.

Complete the format method with the elements contained in flight_matches.
In the first line print the airline,and the flight number.
In the second line, the departure and destination.
In the third line, the date.
"""

# Import re
import re
flight = "Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT"

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

#print(re.findall(regex,flight))

# Find all matches of the flight information
flight_matches = re.findall(regex,flight)
print(flight_matches)
print(flight_matches[0][0])

#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))