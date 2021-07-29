"""
Complete the if-else statement following the instructions.

The text of three movie reviews has been already saved in the variable movies.
You can use print(movies) to view the variable in the IPython Shell.
Instructions

    Find if the substring actor occurs between the characters with index 37 and 41 inclusive.
    If it is not detected, print the statement Word not found.
    Replace actor actor with the substring actor if actor occurs only two repeated times.
    Replace actor actor actor with the substring actor if actor appears three repeated times.

"""
movies = "200    it's clear that he's passionate about his beli...\n" \
         "201    I believe you I always said that the actor act...\n" \
         "202    it's astonishing how frightening the actor act...\n"
#print(movies)

for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))