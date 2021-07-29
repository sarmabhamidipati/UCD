"""
Find the numbers
The variable sentiment_analysis containing the text of one tweet and the re module were loaded in your session.
You can use print() to view it in the IPython Shell.

Write a regex that matches the number of user mentions given as, for example, User_mentions:9 in sentiment_analysis.
Write a regex that matches the number of likes given as, for example, likes: 5 in sentiment_analysis.
Write a regex that matches the number of retweets given as, for example, number of retweets: 4 in sentiment_analysis.
"""
import re
sentiment_analysis = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, " \
                     "number of retweets: 7"

# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))

# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))