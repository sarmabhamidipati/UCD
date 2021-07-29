"""
In this exercise, you'll be revisiting the airlines DataFrame from the previous lesson.

As a reminder, the DataFrame contains flight metadata such as the airline, the destination, waiting times as well as
answers to key questions regarding cleanliness, safety, and satisfaction on the San Francisco Airport.

In this exercise, you will examine two categorical columns from this DataFrame, dest_region and dest_size respectively,
assess how to address them and make sure that they are cleaned and ready for analysis.
The pandas package has been imported as pd, and the airlines DataFrame is in your environment.

Question

From looking at the output, what do you think is the problem with these columns?
Possible Answers

    The dest_region column has only inconsistent values due to capitalization.
    The dest_region column has inconsistent values due to capitalization and has one value that needs to be remapped.
    The dest_size column has only inconsistent values due to leading and trailing spaces.
    Both 2 and 3 are correct.

Both 2 and 3 are correct is the correct answer
"""
import pandas as pd

airlines = pd.read_csv('airlines.csv')
# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())
