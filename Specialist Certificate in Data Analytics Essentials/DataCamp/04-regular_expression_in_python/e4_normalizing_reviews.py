"""
The text of a movie review for only one example has been already saved in the variable movie.
You can use print(movie) to view the variable in the IPython Shell

Convert the string in the variable movie to lowercase. Print the result.
Remove the $ that occur at the start and at the end of the string contained in movie_lower. Print the results.
Split the string contained in movie_no_sign into as many substrings as possible. Print the results.
To get the root of the second word contained in movie_split, select all the characters except the last one.
"""
movie = "$I supposed that coming from MTV Films I should expect no less$"

# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_sign = movie_lower.strip("$")
print(movie_no_sign)

# Split the string into substrings and print the result
movie_split = movie_no_sign.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][:-1]
print(word_root)
