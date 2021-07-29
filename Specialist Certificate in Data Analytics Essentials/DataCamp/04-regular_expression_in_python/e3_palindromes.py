"""
The text of a movie review for one example has been already saved in the variable movie.
You can use print(movie) to view the variable in the IPython Shell.

Instructions
100 XP

    Extract the substring from the 12th to the 30th character from the variable movie which corresponds
    to the movie title. Store it in the variable movie_title.
    Get the palindrome by reversing the string contained in movie_title.
    Complete the code to print out the movie_title if it is a palindrome.

"""
movie = "oh my God! desserts I stressed was an ugly movie"
# Get the word
movie_title = movie[11:30]
print(movie_title)

# Obtain the palindrome
palindrome = movie_title[::-1]
print(palindrome)
# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)