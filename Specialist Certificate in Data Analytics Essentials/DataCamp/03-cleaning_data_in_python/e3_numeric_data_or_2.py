"""
Numeric data or ... ?
In this exercise, and throughout this chapter, you'll be working with bicycle ride sharing data in San Francisco
called ride_sharing. It contains information on the start and end stations, the trip duration,
and some user information for a bike sharing service.

The user_type column contains information on whether a user is taking a free ride and takes on the following values:

    1 for free riders.
    2 for pay per ride.
    3 for monthly subscribers.

In this instance, you will print the information of ride_sharing using .info() and
see a firsthand example of how an incorrect data type can flaw your analysis of the dataset.
The pandas package is imported as pd.

Question

By looking at the summary statistics - they don't really seem to offer much description on
how users are distributed along their purchase type, why do you think that is?
Possible Answers

a. The user_type column is not of the correct type, it should be converted to str.
b. The user_type column has an infinite set of possible values, it should be converted to category.
c. The user_type column has an finite set of possible values that represent groupings of data,
   it should be converted to category.

Answer = c
"""
