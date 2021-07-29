"""
Finding files
The variable sentiment_analysis containing the text of two tweets as well as the re module are already loaded in your
session. You can use print() to view it in the IPython Shell.


    Write a regex that matches the pattern of the text file names, e.g. aemyfile.txt.
    Find all matches of the regex in the elements of sentiment_analysis. Print out the result.
    Replace all matches of the regex with an empty string "". Print out the result.
"""
import re


sentiment_analysis = "780    AIshadowhunters.txt aaaaand back to my literat..." \
                       "781    ouMYTAXES.txt I am worried that I won't get my..."

# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"

for text in sentiment_analysis:
    # Find all matches of the regex
    print(re.findall(regex, text))

    # Replace all matches with empty string
    print(re.sub(regex, "", text))