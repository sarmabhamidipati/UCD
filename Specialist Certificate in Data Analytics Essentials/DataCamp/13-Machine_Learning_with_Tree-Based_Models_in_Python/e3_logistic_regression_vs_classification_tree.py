"""

"""
import e1_train_your_first_classification_tree

# Import LogisticRegression from sklearn.linear_model
from sklearn.linear_model import LogisticRegression
import plot_labeled_decision_regions

# Instatiate logreg
logreg = LogisticRegression(random_state=1)

# Fit logreg to the training set
logreg.fit(e1_train_your_first_classification_tree.X_train, e1_train_your_first_classification_tree.y_train)

# Define a list called clfs containing the two classifiers logreg and dt
clfs = [logreg, e1_train_your_first_classification_tree.dt]

# Review the decision regions of the two classifiers
plot_labeled_decision_regions.plot_labeled_decision_regions(e1_train_your_first_classification_tree.X_test,
                                                            e1_train_your_first_classification_tree.y_test, clfs)
