"""
he text of one movie review has been already saved in the variable movie. You can use print(movie)
to view the variable in the IPython Shell.

Find out how many characters the variable movie has.

Convert the numeric variable length_string to a string representation.

Concatenate the predefined variable statement and the variable to_string adding a space between them.
Print out the result.

"""
movie = "fox and kelley soon become bitter rivals because the new fox books store is opening up right across the " \
        "block from the small business . "
print(movie)
# Find characters in movie variable
length_string = len(movie)

# Convert to string
to_string = str(length_string)

# Predefined variable
statement = "Number of characters in this review:"

# Concatenate strings and print result
print(statement+" "+to_string)