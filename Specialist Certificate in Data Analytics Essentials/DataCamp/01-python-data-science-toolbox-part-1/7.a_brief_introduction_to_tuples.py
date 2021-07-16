'''
A brief introduction to tuples
Instructions

    Unpack nums to the variables num1, num2, and num3.
    Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.

'''
# Unpack nums into num1, num2, and num3
nums = (3,4,6)
num1,num2,num3 = nums
# Construct even_nums
even_nums = (2,num2,num3)
print(even_nums)