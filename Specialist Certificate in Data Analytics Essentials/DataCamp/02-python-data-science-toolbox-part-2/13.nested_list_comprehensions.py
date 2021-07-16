"""
Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row
can be written as:

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

Your task is to recreate this matrix by using nested listed comprehensions. Recall that you can create one of the rows
of the matrix with a single list comprehension. To create the list of lists, you simply have to supply the list
comprehension as the output expression of the overall list comprehension:

Instructions

    In the inner list comprehension - that is, the output expression of the nested list comprehension - create a list of
    values from 0 to 4 using range(). Use col as the iterator variable.
    In the iterable part of your nested list comprehension, use range() to count 5 rows - that is, create a list of values
    from 0 to 4. Use row as the iterator variable; note that you won't be needing this variable to create values
    in the list of lists.

"""
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)

# Create a 3 x 3 matrix using a list of lists: matrix
matrix = [[col for col in range(3)] for row in range(3)]

# Print the matrix
for row in matrix:
    print(row)

# Create a 2 x 2 matrix using a list of lists: matrix
matrix = [[col for col in range(2)] for row in range(2)]

# Print the matrix
for row in matrix:
    print(row)
