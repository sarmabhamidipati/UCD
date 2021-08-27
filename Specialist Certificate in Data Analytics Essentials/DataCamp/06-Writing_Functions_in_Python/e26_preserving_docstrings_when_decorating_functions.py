"""
Preserving docstrings when decorating functions
Decorate print_sum() with the add_hello() decorator to replicate the issue
that your friend saw - that the docstring disappears.

To show your friend that they are printing the wrapper() function's docstring, not the print_sum() docstring,
add the following docstring to wrapper():

Import a function that will allow you to add the metadata from print_sum() to the decorated version of print_sum().

Finally, decorate wrapper() so that the metadata from func() is preserved in the new decorated function.
"""

# Import the function you need to fix the problem
from functools import wraps

def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    # Add a docstring to wrapper
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)

    return wrapper


# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

