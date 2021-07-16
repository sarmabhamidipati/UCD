"""
Numeric data or ... ?
The user_type column contains information on whether a user is taking a free ride and takes on the following values:

    1 for free riders.
    2 for pay per ride.
    3 for monthly subscribers.

In this instance, you will print the information of ride_sharing using .info() and
see a firsthand example of how an incorrect data type can flaw your analysis of the dataset.
The pandas package is imported as pd.

Instructions 1/3
35 XP

    Print the information of ride_sharing.
    Use .describe() to print the summary statistics of the user_type column from ride_sharing.

"""
import pandas as pd
ride_sharing = pd.read_csv('ride_sharing.csv')
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())