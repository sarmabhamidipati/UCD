"""
The list cellphones, containing three phone numbers, and the re module are loaded in your session.
You can use print() to view the data in the IPython Shell.

Get all cell phones numbers that are not preceded by the optional area code.

Get all the cell phones numbers that are not followed by the optional extension.
"""

import re
cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']
for phone in cellphones:
    #Get all phone numbers not preceded by area code
    number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
    print(number)

for phone in cellphones:
	# Get all phone numbers not followed by optional extension
    number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
    print(number)