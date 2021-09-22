"""
Prepare the ground
In the following exercises, you'll compare the OOB accuracy to the test set accuracy of a bagging classifier trained
on the Indian Liver Patient dataset.

In sklearn, you can evaluate the OOB accuracy of an ensemble classifier by setting the parameter oob_score to
True during instantiation. After training the classifier, the OOB accuracy can be obtained by accessing the .oob_score_ attribute from the corresponding instance.

In your environment, we have made available the class DecisionTreeClassifier from sklearn.tree.
Instructions
100 XP

    Import BaggingClassifier from sklearn.ensemble.

    Instantiate a DecisionTreeClassifier with min_samples_leaf set to 8.

    Instantiate a BaggingClassifier consisting of 50 trees and set oob_score to True.

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('indian_liver_patient.csv')

print(df.info())
df = df.dropna()
# print(df.info())


df['Dataset'] = df['Dataset'].apply((lambda x: 1 if x == 1 else 0))

# print(df.head(10))

X = df.drop('Dataset', axis=1)
y = df['Dataset']

# print(X.head())
# print(X.info())

labelencoder_gender = LabelEncoder()

X.iloc[:, 1] = labelencoder_gender.fit_transform(X.iloc[:, 1].values)
# print(X.head())
# print(type(y))
# print(y.head(10))

print(X.dtypes)
print(X.info())

# Set seed for reproducibility
SEED = 1

# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    stratify=y,
                                                    random_state=SEED)

# Instantiate dt
dt = DecisionTreeClassifier(min_samples_leaf=8, random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt,
                       n_estimators=50,
                       oob_score=True,
                       random_state=1)
