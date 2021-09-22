"""
Using entropy as a criterion
n this exercise, you'll train a classification tree on the Wisconsin Breast Cancer dataset using entropy
as an information criterion. You'll do so using all the 30 features in the dataset, which is split into 80% train and 20% test.

X_train as well as the array of labels y_train are available in your workspace.

"""

import e1_train_your_first_classification_tree
# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier

# Instantiate dt_entropy, set 'entropy' as the information criterion
dt_entropy = DecisionTreeClassifier(max_depth=8, criterion='entropy', random_state=1)


# Fit dt_entropy to the training set
dt_entropy.fit(e1_train_your_first_classification_tree.X_train, e1_train_your_first_classification_tree.y_train)


