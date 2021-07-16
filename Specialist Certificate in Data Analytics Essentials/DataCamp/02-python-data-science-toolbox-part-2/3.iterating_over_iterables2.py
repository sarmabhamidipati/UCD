'''
Iterating over iterables (2)

The value is actually what's called a Googol which is a 1 followed by a hundred 0s. That's a huge number!

Instructions


    Create an iterator object small_value over range(3) using the function iter().
    Using a for loop, iterate over range(3), printing the value for every iteration. Use num as the loop variable.
    Create an iterator object googol over range(10 ** 100).
'''
# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
