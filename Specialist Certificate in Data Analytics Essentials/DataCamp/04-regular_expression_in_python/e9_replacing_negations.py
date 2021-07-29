"""
Replacing negations
The text of this column has been already saved in the variable movies so you start working with it.
You can use print(movies) to view it in the IPython Shell.
Instructions
100 XP

    Replace the substring isn't with the word is.
    Replace the substring important with the word insignificant.
    Print out the result contained in the variable movies_antonym.

"""
movies = "the rest of the story isn't important because all it does is serve as a mere backdrop for the two starsto " \
         "share the screen . "

print(movies)

# Replace negations
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)