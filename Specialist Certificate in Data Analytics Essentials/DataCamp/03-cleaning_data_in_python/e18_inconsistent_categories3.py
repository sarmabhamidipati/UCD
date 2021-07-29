"""
Inconsistent categories

In this exercise, you'll be revisiting the airlines DataFrame from the previous lesson.

As a reminder, the DataFrame contains flight metadata such as the airline, the destination, waiting times as well as
answers to key questions regarding cleanliness, safety, and satisfaction on the San Francisco Airport.

In this exercise, you will examine two categorical columns from this DataFrame, dest_region and dest_size respectively,
assess how to address them and make sure that they are cleaned and ready for analysis.
The pandas package has been imported as pd, and the airlines DataFrame is in your environment.

Instructions 3/4

    Change the capitalization of all values of dest_region to lowercase.
    Replace the 'eur' with 'europe' in dest_region using the .replace() method.

"""
import pandas as pd

airlines = pd.read_csv('airlines.csv')

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur': 'europe'})
