"""
Import data for Supervised Learning in Machine learning. Here we are using auto.csv which contains
data about cars regarding its miles per gallon based on 6 features
(mpg,	displ,	hp,	weight,	accel,	origin,	size)
"""

import pandas as pd
# Import train_test_split
from sklearn.model_selection import train_test_split

df = pd.read_csv('auto.csv')

#print(df.info())

df1 = pd.get_dummies(df.origin, prefix='origin')

#print(df1.info())

df = df.join(df1)
print(df.info())

# Getting Features
X = df[['displ', 'hp', 'weight', 'accel', 'size', 'origin_Asia', 'origin_Europe', 'origin_US']]

# Getting Predicting Value
y = df['mpg']

print(X)
print(y)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

#print(X_train)
#print(y_train)
