import pandas as pd
df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

print(df)

other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],'B': ['B0', 'B1', 'B2']})
print(other)

# Join DataFrames using their indexes.
print(df.join(other, lsuffix='_caller', rsuffix='_other'))

#If we want to join using the key columns, we need to set key to be the index in both df and other.
#The joined DataFrame will have key as its index.
print(df.set_index('key').join(other.set_index('key')))

#Another option to join using the key columns is to use the on parameter.
#DataFrame.join always uses other’s index but we can use any column in df.
#This method preserves the original DataFrame’s index in the result.

print(df.join(other.set_index('key'), on='key'))