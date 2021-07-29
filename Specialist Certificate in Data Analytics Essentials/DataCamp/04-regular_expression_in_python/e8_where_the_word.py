"""
The text of two movie reviews has been already saved in the variable movies.
You can use print(movies) to view the variable in the IPython Shell.

Find the index where money occurs between characters with index 12 and 50. If not found, the method should return -1.
Find the index where money occurs between characters with index 12 and 50. If not found, it should raise an error.
"""
movies = "137    heck , jackie doesn't even have enough money f...\n" \
         "138    in condor , chan plays the same character he's..."
print(movies)

for movie in movies:
    # Find the first occurrence of word
    print(movie.find("money", 12, 51))
    break

for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index("money", 12, 51))
  except ValueError:
    print("substring not found")
    break