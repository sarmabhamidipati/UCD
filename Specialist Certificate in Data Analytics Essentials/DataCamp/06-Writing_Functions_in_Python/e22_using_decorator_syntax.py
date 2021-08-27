"""
Using decorator syntax
You have written a decorator called print_args that prints out all of the arguments and their values
any time a function that it is decorating gets called.
Decorate my_function() with the print_args() decorator using decorator syntax.
"""

def print_args(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    return func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_args
def my_function(a, b):
  print(a + b)

my_function(5, 10)