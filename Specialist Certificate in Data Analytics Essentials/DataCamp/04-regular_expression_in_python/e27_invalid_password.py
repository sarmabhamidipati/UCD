"""
Invalid password
The list passwords and the module re are loaded in your session.
You can use print(passwords) to view them in the IPython Shell.

    Write a regular expression to match valid passwords as described.
    Scan the elements in the passwords list to find out if they are valid passwords.
    To print out the message indicating if it is a valid password or not, complete .format() statement.

"""
import re
passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']

# Write a regex to match a valid password
regex = r"[a-zA-Z0-9*#$%!&.]{8,}"

for example in passwords:
  	# Scan the strings to find a match
    if re.findall(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))