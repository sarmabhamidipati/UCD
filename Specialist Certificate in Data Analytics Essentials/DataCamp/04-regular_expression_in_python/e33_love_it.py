"""
Love it!
The list sentiment_analysis containing the text of three tweets and the re module are loaded in your session.
You can use print() to view the data in the IPython Shell.


    Complete the regular expression to capture the words love or like or enjoy.
    Match and capture the words movie or concert. Match and capture anything appearing until the ..
    Find all matches of the regex in each element of sentiment_analysis. Assign them to positive_matches.
    Complete the .format() method to print out the results contained
    in positive_matches for each element in sentiment_analysis.

"""

import re
sentiment_analysis = ['I totally love the concert The Book of Souls World Tour. It kinda amazing!', 'I enjoy the '
                                                                                                    'movie Wreck-It '
                                                                                                    'Ralph. I watched '
                                                                                                    'with my '
                                                                                                    'boyfriend.',
                      "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]

# Write a regex that matches sentences with the optional words
# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)

    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))