"""
Dict comprehensions
You are given a list of strings fellowship and, using a dict comprehension, create a dictionary with the members of the
 list as the keys and the length of each string as the corresponding values.

Instructions

    Create a dict comprehension where the key is a string in fellowship and the value is the length of the string.
    Remember to use the syntax <key> : <value> in the output expression part of the comprehension to create the members
    of the dictionary. Use member as the iterator variable.
"""
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)
