"""
Surrounding words
Positive lookahead (?=) makes sure that first part of the expression is followed by the lookahead expression.
Positive lookbehind (?<=) returns all matches that are preceded by the specified pattern.

The variable sentiment_analysis, containing the text of one tweet, and the re module are loaded in your session.
You can use print() to view the data in the IPython Shell.

Get all the words that are followed by the word python in sentiment_analysis. Print out the word found.

Get all the words that are preceded by the word python or Python in sentiment_analysis. Print out the words found.
"""

import re

sentiment_analysis = "You need excellent python skills to be a data scientist. Must be! Excellent python"

# Positive lookahead
look_ahead = re.findall(r"\w+.(?=\spython)", sentiment_analysis)


# Print out
print(look_ahead)

# Positive lookbehind
look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)