"""
Understanding the difference

The string is already loaded as string to your session.

    Import the re module.
    Write a regex expression to replace HTML tags with an empty string.
    Print out the result.

"""
# Import re
import re
string = "I want to see that <strong>amazing show</strong> again!"
print(string)
#string_notags = re.sub(r"<|>|/", " ", string)
string_notags = re.sub(r"<.+?>", " ", string)

# Print out the result
print(string_notags)