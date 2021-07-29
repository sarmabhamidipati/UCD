"""
Parsing PDF files
The variable contract containing the text of one contract and the re module are already loaded in your session.
You can use print() to view the data in the IPython Shell.
Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches.
Assign each captured group to the corresponding keys in the dictionary.
Complete the positional method to print out the captured groups.
Use the values corresponding to each key in the dictionary.
"""
import re

contract = "Provider will invoice Client for Services performed within 30 days of performance.  Client will pay " \
           "Provider as set forth in each Statement of Work within 30 days of receipt and acceptance of such invoice. " \
           "It is understood that payments to Provider for services rendered shall be made in full as agreed, " \
           "without any deductions for taxes of any kind whatsoever, in conformity with Provider’s status as an " \
           "independent contractor. Signed on 03/25/2001. "
# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)
print(dates.group(0))
print(dates.group(1))
print(dates.group(2))
print(dates.group(3))

# Assign to each key the corresponding match
signature = {
    "day": dates.group(2),
    "month": dates.group(1),
    "year": dates.group(3)
}

print(signature["day"], signature["month"], signature["year"])

# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. "
      "Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))
