"""
Crafting a docstring
The first function you write is count_letter(). It takes a string and a single letter and
returns the number of times the letter appears in the string.
Build up a Google Style docstring for this function by following these steps.
Copy the following string and add it as the docstring for the function:
Count the number of times `letter` appears in `content`.
"""


# Add a docstring to count_letter()
def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    # Add a Google style arguments section
    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    # Add a returns section
    Returns:
      int:
    # Add a section detailing what errors might be raised
    Raises:
    ValueError: If `letter` is not a one-character string.

    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])
