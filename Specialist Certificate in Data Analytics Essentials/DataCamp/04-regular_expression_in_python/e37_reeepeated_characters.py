"""
Reeepeated characters
The list sentiment_analysis, containing the text of three tweets, and the re module are loaded in your session.
You can use print() to view the data in the IPython Shell.


    Complete the regular expression to match an elongated word as described.
    Search the elements in sentiment_analysis list to find out if they contain elongated words.
    Assign the result to match_elongated.
    Assign the captured group number zero to the variable elongated_word.
    Print the result contained in the variable elongated_word.

"""
import re
sentiment_analysis = ['@marykatherine_q i know! I heard it this morning and wondered the same thing. '
                      'Moscooooooow is so behind the times',
                      'Staying at a friends house...neighborrrrrrrs are so loud-having a party',
                      'Just woke up an already have read some e-mail']

# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
    # Find if there is a match in each tweet
    match_elongated = re.search(regex_elongated, tweet)

    if match_elongated:
        # Assign the captured group zero
        elongated_word = match_elongated.group(0)

        # Complete the format method to print the word
        print("Elongated word found: {word}".format(word=elongated_word))
    else:
        print("No elongated word found")