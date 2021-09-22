"""
Entropy vs Gini index
In this exercise you'll compare the test set accuracy of dt_entropy to the accuracy of another tree named dt_gini.
The tree dt_gini was trained on the same dataset using the same parameters except for the information criterion
which was set to the gini index using the keyword 'gini'.

X_test, y_test, dt_entropy, as well as accuracy_gini which corresponds to the test set accuracy
achieved by dt_gini are available in your workspace.
"""


import e1_train_your_first_classification_tree
# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

accuracy_gini = 0.92982456140350878

# Instantiate dt_entropy, set 'entropy' as the information criterion
dt_entropy = DecisionTreeClassifier(max_depth=8, criterion='entropy', random_state=1)


# Fit dt_entropy to the training set
dt_entropy.fit(e1_train_your_first_classification_tree.X_train, e1_train_your_first_classification_tree.y_train)

# Use dt_entropy to predict test set labels
y_pred = dt_entropy.predict(e1_train_your_first_classification_tree.X_test)

# Evaluate accuracy_entropy
accuracy_entropy = accuracy_score(e1_train_your_first_classification_tree.y_test, y_pred)

# Print accuracy_entropy
print('Accuracy achieved by using entropy: ', accuracy_entropy)

# Print accuracy_gini
print('Accuracy achieved by using the gini index: ', accuracy_gini)