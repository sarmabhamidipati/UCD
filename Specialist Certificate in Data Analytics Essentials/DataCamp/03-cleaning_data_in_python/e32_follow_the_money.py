"""
In this exercise, you will drop rows of banking with missing cust_ids, and impute missing values of acct_amount
with some domain knowledge.
Instructions


    Use .dropna() to drop missing values of the cust_id column in banking and store the results in banking_fullid.
    Compute the estimated acct_amount of banking_fullid knowing that acct_amount is usually inv_amount * 5 and
    assign the results to acct_imp.
    Impute the missing values of acct_amount in banking_fullid with the newly created acct_imp using .fillna().

"""
import pandas as pd

# import missingno as msno
# import matplotlib.pyplot as plt

banking = pd.read_csv('banking2.csv')

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset=['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())
