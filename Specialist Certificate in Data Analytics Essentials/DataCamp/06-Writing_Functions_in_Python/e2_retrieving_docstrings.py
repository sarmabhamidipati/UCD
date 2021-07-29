"""
Retrieving docstrings
You will be reusing the count_letter() function that you developed in the last exercise to show that we can
properly extract its docstring.
Now create a build_tooltip() function that can extract the docstring from any function that we pass to it.
"""
from crafting_a_docstring import count_letter
import inspect

# Get the "count_letter" docstring by using an attribute of the function
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

# Inspect the count_letter() function to get its docstring
docstring = inspect.getdoc(count_letter)
border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))


def build_tooltip(function):
    """Create a tooltip for any function that shows the
  function's docstring.

  Args:
    function (callable): The function we want a tooltip for.

  Returns:
    str
  """
    # Get the docstring for the "function" argument by using inspect
    docstring = inspect.getdoc(function)
    border = '#' * 28
    return '{}\n{}\n{}'.format(border, docstring, border)


print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
