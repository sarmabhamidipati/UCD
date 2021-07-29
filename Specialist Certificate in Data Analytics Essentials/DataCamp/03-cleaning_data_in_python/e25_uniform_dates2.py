"""
Instructions 2/4

Question

Take a look at the output. You tried converting the values to datetime using the default to_datetime() function
without changing any argument, however received the following error:

ValueError: month must be in 1..12

Why do you think that is?

Possible Answers

    The to_datetime() function needs to be explicitly told which date format each row is in.
    The to_datetime() function can only be applied on YY-mm-dd date formats.
    The 21-14-17 entry is erroneous and leads to an error.
Answer : C
"""
import pandas as pd

banking = pd.read_csv('banking.csv')
print(banking)

# Print the header of account_opened
print(banking['account_opened'].head())

print(pd.to_datetime(banking['account_opened']))
