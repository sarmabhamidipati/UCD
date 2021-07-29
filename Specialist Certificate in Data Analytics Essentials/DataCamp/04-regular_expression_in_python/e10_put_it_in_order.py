"""
The text of one article has already been saved in the variable wikipedia_article. Also, the empty list my_list is
already defined. You can use print() to view the variable in the IPython Shell.

Assign the substrings going from the 4th to the 19th character inclusive, and from the 22nd to the 44th character
inclusive of wikipedia_article to the variables first_pos and second_pos,
respectively. Adjust the strings to be lowercase.

Define a string with the text "The tool is used in" adding placeholders after the word tool and the word in
for future positional formatting. Append it to the list my_list.

Define a string with the text "The tool is used in" adding placeholders after the word tool and in but reorder them
so the second argument passed to the method will replace the first placeholder. Append to the list my_list.

Complete the for-loop so that it uses the .format() method and
the variables first_pos and second_pos to print out every string in my_list.
"""

wikipedia_article = "In computer science, artificial intelligence (AI), sometimes called machine intelligence, " \
                    "is intelligence demonstrated by machines, in contrast to the natural intelligence displayed " \
                    "by humans and animals."
my_list = []

print(wikipedia_article)
print(my_list)

# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()
print(first_pos)
print(second_pos)

my_string = "The tool {} is used in {}"

# Define string with placeholders
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0} ")

# Use format to print strings
for my_string in my_list:
    print(my_string.format(first_pos, second_pos))
