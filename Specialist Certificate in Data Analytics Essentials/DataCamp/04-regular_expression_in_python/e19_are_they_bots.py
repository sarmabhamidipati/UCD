"""
Are they bots?
The text of one tweet was saved in the variable sentiment_analysis.
You can use print(sentiment_analysis) to view it in the IPython Shell.

    Import the re module.
    Write a regex that matches the user mentions that starts with @ and follows the pattern, e.g. @robot3!.
    Find all the matches of the pattern in the sentiment_analysis variable.

"""
# Import the re module
import re

sentiment_analysis = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"


# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))