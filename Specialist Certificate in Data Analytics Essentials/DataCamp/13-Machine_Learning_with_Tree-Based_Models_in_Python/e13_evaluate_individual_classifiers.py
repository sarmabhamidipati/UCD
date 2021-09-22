"""
Evaluate individual classifiers
In this exercise you'll evaluate the performance of the models in the list classifiers that we defined in the
previous exercise. You'll do so by fitting each classifier on the training set and evaluating its test set accuracy.
Instructions
100 XP

    Iterate over the tuples in classifiers. Use clf_name and clf as the for loop variables:
        Fit clf to the training set.
        Predict clf's test set labels and assign the results to y_pred.
        Evaluate the test set accuracy of clf and print the result.

"""
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import accuracy_score

df = pd.read_csv('indian_liver_patient_preprocessed.csv')

# Getting Features
X = df.drop('Liver_disease', axis=1)
#print(X)

# Getting Predicting Value
y = df['Liver_disease']
#print(y)

# Set seed for reproducibility
SEED=1

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Instantiate lr
lr = LogisticRegression(random_state=SEED)

# Instantiate knn
knn = KNN(n_neighbors=27)

# Instantiate dt
dt = DecisionTreeClassifier(min_samples_leaf=0.13, random_state=SEED)

# Define the list classifiers
classifiers = [('Logistic Regression', lr), ('K Nearest Neighbours', knn), ('Classification Tree', dt)]

# Iterate over the pre-defined list of classifiers
for clf_name, clf in classifiers:
    # Fit clf to the training set
    clf.fit(X_train, y_train)

    # Predict y_pred
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Evaluate clf's accuracy on the test set
    print('{:s} : {:.3f}'.format(clf_name, accuracy))
