"""
The text of the file has been already saved in the variable file.
You can use print(file) to view the variable in the IPython Shell.


    Split the string file into many substrings at line boundaries.
    Print out the resulting variable file_split.
    Complete the for-loop to split the strings into many substrings using commas as a separator element.

"""
import substring as substring

file = "mtv films election, a high school comedy, is a current example \n" \
       "from there, director steven spielberg wastes no time, taking us into the water on a midnight swim "
print(file)

# Split string at line boundaries
file_split = file.split(sep="\n")

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(sep=",")
    print(substring_split)
