"""
Everything clean
The list sentiment_analysis containing the text of three tweet are already loaded in your session.
You can use print() to view the data in the IPython Shell.

Instructions

    Import the re module.
    Write a regex to find all the matches of http links appearing in each tweet in sentiment_analysis.
    Print out the result.
    Write a regex to find all the matches of user mentions appearing in each tweet in sentiment_analysis.
    Print out the result.

"""

# Import re module
import re

sentiment_analysis = "Boredd. Colddd @blueKnight39 Internet keeps stuffing up. Save me! https://www.tellyourstory.com" \
    "I had a horrible nightmare last night @anitaLopez98 @MyredHat31 which affected my sleep, now I'm really tired" \
    "im lonely  keep me company @YourBestCompany! @foxRadio https://radio.foxnews.com 22 female, new york"

for tweet in sentiment_analysis:
    # Write regex to match http links and print out result
    print(re.findall(r"http\S+", tweet))

    # Write regex to match user mentions and print out result
    print(re.findall(r"@\w+", tweet))