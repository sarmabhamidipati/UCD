"""
List comprehensions for time-stamped data
In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data.
The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the df DataFrame for your use.

Instructions

    Extract the column 'created_at' from df and assign the result to tweet_time. Fun fact: the extracted column in
    tweet_time here is a Series data structure!
    Create a list comprehension that extracts the time from each row in tweet_time. Each row is a string that
    represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time.
    Use entry as the iterator variable and assign the result to tweet_clock_time.
    Remember that Python uses 0-based indexing!

"""
import pandas as pd
df = pd.Series('tweets.csv')
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)
