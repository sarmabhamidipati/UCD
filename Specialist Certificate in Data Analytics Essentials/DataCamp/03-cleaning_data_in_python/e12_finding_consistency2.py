"""
The DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key
questions regarding cleanliness, safety, and satisfaction. Another DataFrame named categories was created, containing
all correct possible values for the survey columns.

In this exercise, you will use both of these DataFrames to find survey answers with inconsistent values,
and drop them, effectively performing an outer and inner join on both these DataFrames as seen in the video exercise.
The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment.

Question

Take a look at the output. Out of the cleanliness, safety and satisfaction columns,
which one has an inconsistent category and what is it?

Take a look at the output. Out of the cleanliness, safety and satisfaction columns, which one has an inconsistent category and what is it?
Possible Answers

    cleanliness because it has an Unacceptable category.
    cleanliness because it has a Terribly dirty category.
    satisfaction because it has a Very satisfied category.
    safety because it has a Neutral category.
Answer : A
"""
import pandas as pd
categories = pd.read_csv('categories.csv')
airlines = pd.read_csv('airlines.csv')

print(categories)
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Cleanliness: ', airlines['safety'].unique(), "\n")
print('Cleanliness: ', airlines['satisfaction'].unique(), "\n")
