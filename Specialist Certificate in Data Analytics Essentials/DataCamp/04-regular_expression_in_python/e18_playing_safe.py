"""
The answer of one user has been stored in the dictionary answers.
You can use the print() function to view the variables in the IPython Shell.
Complete the template string using $answer1 and $answer2 as identifiers.

Use the method .substitute() to replace the identifiers with the values in answers in the predefined template.
Use the method .safe_substitute() to replace the identifiers with the values in answers in the predefined template.
"""
# Import template
from string import Template

answers = {'answer1': 'I really like the app. But there are some features that can be improved'}

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use substitute to replace identifiers
try:
    print(the_answers.substitute(answers))
except KeyError:
    print("Missing information")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")