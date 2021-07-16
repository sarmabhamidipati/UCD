"""
List comprehensions vs generators

generators does not store data in memnory like list

if there a very large list then use generators.
There is no point in using large list instead use generators

In this exercise, you will recall the difference between list comprehensions and generators. To help with that task,
the following code has been pre-loaded in the environment:

# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)

Try to play around with fellow1 and fellow2 by figuring out their types and printing out their values. Based on your
observations and what you can recall from the video, select from the options below the best description for the
difference between list comprehensions and generators.
Instructions
Possible Answers

    1.List comprehensions and generators are not different at all; they are just different ways of
      writing the same thing.
    2.A list comprehension produces a list as output, a generator produces a generator object.
    3.A list comprehension produces a list as output that can be iterated over, a generator produces a generator object
      that can't be iterated over.
    Answer : 2

"""

# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)

print(fellow1)
print(fellow2)