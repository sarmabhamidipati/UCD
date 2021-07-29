"""
The text of a movie review has been already saved in the variable movie.
You can use print(movie) to view the variable in the IPython Shell.

Remove tag <\i> from the end of the string. Print the results.
Split the string contained in movie_tag using the commas as a separating element. Print the results.
Join back together the list of substring contained in movie_no_comma using a space as a join element. Print the results.
"""
movie = "the film,however,is all good<\i>"
print(movie)
# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(sep=",")
print(movie_no_comma)

# Join back together and print results
movie_join = " ".join(movie_no_comma)
print(movie_join)