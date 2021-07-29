"""
You just received a new version of the banking DataFrame containing data on the amount held and invested for new
and existing customers. However, there are rows with missing inv_amount values.

You know for a fact that most customers below 25 do not have investment accounts yet, and suspect it could be driving
the missingness. The pandas, missingno and matplotlib.pyplot packages have been imported as pd, msno and plt
respectively. The banking DataFrame is in your environment.
Instructions 1/4

    Print the number of missing values by column in the banking DataFrame.
    Plot and show the missingness matrix of banking with the msno.matrix() function.

Isolate the values of banking missing values of inv_amount into missing_investors and
with non-missing inv_amount values into investors.

Question 3

Now that you've isolated banking into investors and missing_investors, use the .describe() method on both of
these DataFrames in the console to understand whether there are structural differences between them.
What do you think is going on?

Sort the banking DataFrame by the age column and plot the missingness matrix of banking_sorted.
"""
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

banking = pd.read_csv('banking2.csv')
# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
#plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

print(investors.describe())
print(missing_investors.describe())
"""
A.The data is missing completely at random and there are no drivers behind the missingness.

B.The inv_amount is missing only for young customers, since the average age in missing_investors is 22 
and the maximum age is 25.

C. The inv_amount is missing only for old customers, since the average age in missing_investors is 42 
and the maximum age is 59.

Answer = B
"""

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()