"""
Importing data for supervised learning
"""

import pandas as pd
# Import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('breast_cancer_data.csv')

# print(df.head(5))
# print(df.info())
df.drop('Unnamed: 32', axis=1, inplace=True)

# Getting Features
X = df[['radius_mean', 'concave points_mean']]

print('Type of X : ', type(X))
print('info of X : ', X.info())


# Getting Predicting Value
le = LabelEncoder()
diagnosis_encoded = le.fit_transform(df['diagnosis'])
df['diagnosis'] = diagnosis_encoded

# Getting Predicting Value
y = df['diagnosis']

print('Type of y : ', type(y))
print('data of y : ')
print(y)



# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=1)

print(X_train)
print(X_test)

print(y_train)
print(y_test)
