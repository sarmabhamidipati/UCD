"""
Evaluate the AdaBoost classifier
Now that you're done training ada and predicting the probabilities of obtaining the positive class in the test set,
it's time to evaluate ada's ROC AUC score. Recall that the ROC AUC score of a binary classifier can be determined
using the roc_auc_score() function from sklearn.metrics.

The arrays y_test and y_pred_proba that you computed in the previous exercise are available in your workspace.

Instructions
100 XP

    Import roc_auc_score from sklearn.metrics.

    Compute ada's test set ROC AUC score, assign it to ada_roc_auc, and print it out.

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
# Import AdaBoostClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder
# Import roc_auc_score
from sklearn.metrics import roc_auc_score


df = pd.read_csv('indian_liver_patient.csv')

# print(df.info())
df = df.dropna()
# print(df.info())


df['Dataset'] = df['Dataset'].apply((lambda x: 1 if x == 1 else 0))

# print(df.head(10))

X = df.drop('Dataset', axis=1)
y = df['Dataset']

labelencoder_gender = LabelEncoder()

X.iloc[:, 1] = labelencoder_gender.fit_transform(X.iloc[:, 1].values)


# Set seed for reproducibility
SEED = 1
# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    stratify=y,
                                                    random_state=SEED)
# Instantiate dt
dt = DecisionTreeClassifier(max_depth=2, random_state=1)

# Instantiate ada
ada = AdaBoostClassifier(base_estimator=dt, n_estimators=180, random_state=1)

# Fit ada to the training set
ada.fit(X_train, y_train)

# Compute the probabilities of obtaining the positive class
y_pred_proba = ada.predict_proba(X_test)[:, 1]


# Evaluate test-set roc_auc_score
ada_roc_auc = roc_auc_score(y_test, y_pred_proba)

# Print roc_auc_score
print('ROC AUC score: {:.2f}'.format(ada_roc_auc))
