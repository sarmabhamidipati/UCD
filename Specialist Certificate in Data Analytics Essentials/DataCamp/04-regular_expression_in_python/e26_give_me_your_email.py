"""
Give me your email

The list emails as well as the re module are loaded in your session.
You can use print(emails) to view the emails in the IPython Shell.


    Write a regular expression to match valid email addresses as described.
    Match the regex to the elements contained in emails.
    To print out the message indicating if it is a valid email or not, complete .format() statement.

"""
import re

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
# Write a regex to match a valid email address
regex = r"[a-zA-Z0-9]+@\w+\.com"

for example in emails:
    # Match the regex to the string
    if re.findall(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))
