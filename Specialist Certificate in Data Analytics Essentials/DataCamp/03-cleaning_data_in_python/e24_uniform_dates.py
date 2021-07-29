"""
After having unified the currencies of your different account amounts, you want to add a temporal dimension to your
analysis and see how customers have been investing their money given the size of their account over each year.
The account_opened column represents when customers opened their accounts and is a good proxy
for segmenting customer activity and investment over time.

However, since this data was consolidated from multiple sources, you need to make sure that all dates are of the
same format. You will do so by converting this column into a datetime object, while making sure that the format is
inferred and potentially incorrect formats are set to missing.
The banking DataFrame is in your environment and pandas was imported as pd.

Instructions 1/4

    Print the header of account_opened from the banking DataFrame and take a look at the different results.

"""
import pandas as pd

banking = pd.read_csv('banking.csv')
print(banking)

# Print the header of account_opened
print(banking['account_opened'].head())
