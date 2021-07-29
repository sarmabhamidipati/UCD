"""
The list sentiment_analysis containing the text of three tweets as well as the re module were loaded in your session.
You can use print() to view it in the IPython Shell.


Complete the regex to match the email capturing only the name part. The name part appears before the @.
Find all matches of the regex in each element of sentiment_analysis analysis. Assign it to the variable email_matched.
Complete the .format() method to print the results captured in each element of sentiment_analysis analysis.

"""
import re

sentiment_analysis = [
    'Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices',
    'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.',
    'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']


# Write a regex that matches email
regex_email = r"([a-zA-Z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))