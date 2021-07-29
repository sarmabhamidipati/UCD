"""
Instructions 3/4

    Convert the account_opened column to datetime, while making sure the date format is inferred and
    that erroneous formats that raise error return a missing value.

"""
import pandas as pd

banking = pd.read_csv('banking.csv')
print(banking)

print(pd.to_datetime(banking['account_opened'], infer_datetime_format=True, errors='coerce'))
