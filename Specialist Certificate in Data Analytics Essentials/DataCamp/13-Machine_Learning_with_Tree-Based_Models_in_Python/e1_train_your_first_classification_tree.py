"""
Train your first classification tree
In this exercise you'll work with the Wisconsin Breast Cancer Dataset from the UCI machine learning repository.
You'll predict whether a tumor is malignant or benign based on two features: the mean radius of the tumor (radius_mean)
and its mean number of concave points (concave points_mean).

The dataset is already loaded in your workspace and is split into 80% train and 20% test.
The feature matrices are assigned to X_train and X_test, while the arrays of labels are assigned to y_train and
y_test where class 1 corresponds to a malignant tumor and class 0 corresponds to a benign tumor.
To obtain reproducible results, we also defined a variable called SEED which is set to 1.

"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier

# read csv file

df = pd.read_csv('breast_cancer_data.csv')
df.drop('Unnamed: 32', axis=1, inplace=True)

# Getting Features
X = df[['radius_mean', 'concave points_mean']]

# convert categorical data to one hot encoding
le = LabelEncoder()
diagnosis_encoded = le.fit_transform(df['diagnosis'])
df['diagnosis'] = diagnosis_encoded
# Getting Predicting Value
y = df['diagnosis']

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=1)

# Instantiate a DecisionTreeClassifier 'dt' with a maximum depth of 6

dt = DecisionTreeClassifier(max_depth=6, random_state=1)

# Fit dt to the training set
dt.fit(X_train, y_train)

# Predict test set labels
y_pred = dt.predict(X_test)
print(y_pred[0:5])
