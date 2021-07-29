"""
Literally formatting
The variables field1, field2 and field3 containing character strings as well
as the numeric variables fact1, fact2, fact3 and fact4 have been saved.

If you want to explore the variables, you can use print() to view them in the IPython Shell.

Complete the f-string to include the variable field1 with quotes and the variable fact1 as a digit.

Complete the f-string to include the variable fact2 using exponential notation, and the variable field2.

Complete the f-string to include field3 together with fact3 rounded to 2 decimals, and fact4 rounded to one decimal.
"""
field1 = "sexiest job"
field2 = "data is produced daily"
field3 = "Individuals"
fact1 = 21
fact2 = 2500000000000000000
fact3 = 72.41415415151
fact4 = 1.09

# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1}st century")

# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")

# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

