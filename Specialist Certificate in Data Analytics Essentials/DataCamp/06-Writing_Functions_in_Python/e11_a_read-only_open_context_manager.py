"""
A read-only open() context manager

    Yield control from open_read_only() to the context block, ensuring that the read_only_file object
    gets assigned to my_file.
    Use read_only_file's .close() method to ensure that you don't leave open files lying around.
"""
from contextlib import contextmanager
import time


@contextmanager
def open_read_only(filename):
    """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
    read_only_file = open(filename, mode='r')
    # Yield read_only_file so it can be assigned to my_file
    yield read_only_file
    # Close read_only_file
    read_only_file.close()


with open_read_only('my_file.txt') as my_file:
    print(my_file.read())