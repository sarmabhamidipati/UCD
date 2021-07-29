"""
The text of two movie reviews has been already saved in the variables movie1 and movie2.
You can use the print() function to view the variables in the IPython Shell.

Remember: The 1st character of a string has index 0.

Instructions
Select the first 32 characters of the variable movie1 and assign it to the variable first_part.
Select the substring going from the 43rd character to the end of movie1. Assign it to the variable last_part.
Select the substring going from the 33rd to the 42nd character of movie2. Assign it to the variable middle_part.
Print the concatenation of the variables first_part, middle_part and last_part in that order.
Print the variable movie2 and compare them.
"""

movie1 = "the most significant tension of _election_ is the potential relationship between a teacher and his student ."
movie2 = "the most significant tension of _rushmore_ is the potential relationship between a teacher and his student ."

first_part = movie1[:32]
print(first_part)

# Select from 43rd character to the end of movie1
last_part = movie1[42:]
print(last_part)

# Select from 33rd to the 42nd character of movie2
middle_part = movie2[32:42]
print(middle_part)

# Print concatenation and movie2 variable
print(first_part+middle_part+last_part)
print(movie2)