"""
Instructions 4/4

    Extract the year from the amended account_opened column and assign it to the acct_year column.
    Print the newly created acct_year column.

"""
import pandas as pd

banking = pd.read_csv('banking.csv')

# Print the header of account_opend
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format=True,
                                           # Return missing value for error
                                           errors='coerce')

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])
