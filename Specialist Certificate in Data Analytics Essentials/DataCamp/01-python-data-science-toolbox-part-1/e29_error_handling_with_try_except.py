'''
Error handling with try-except
In this exercise, you will define a function as well as use a try-except block for handling
cases when incorrect input arguments are passed to the function.

Instructions

    Initialize the variables echo_word and shout_words to empty strings.
    Add the keywords try and except in the appropriate locations for the exception handling block.
    Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
    Concatenate the string '!!!' to echo_word. Assign the result to shout_words.

'''
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word,shout_words = '',''

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1*echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'

    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")