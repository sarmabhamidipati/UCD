"""
Write your own generator expressions
Now, you will start simple by creating a generator object that produces numeric values.

Instructions

    Create a generator object that will produce values from 0 to 30. Assign the result to result and use num as the
    iterator variable in the generator expression.
    Print the first 5 values by using next() appropriately in print().
    Print the rest of the values by using a for loop to iterate over the generator object.

"""
# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)
