"""
Train the AdaBoost classifier
Now that you've instantiated the AdaBoost classifier ada, it's time train it. You will also predict the probabilities
of obtaining the positive class in the test set. This can be done as follows:

Once the classifier ada is trained, call the .predict_proba() method by passing X_test as a parameter and extract
these probabilities by slicing all the values in the second column as follows:

ada.predict_proba(X_test)[:,1]

The Indian Liver dataset is processed for you and split into 80% train and 20% test.
Feature matrices X_train and X_test, as well as the arrays of labels y_train and y_test are available in your workspace.
 In addition, we have also loaded the instantiated model ada from the previous exercise.

 Instructions
100 XP

    Fit ada to the training set.

    Evaluate the probabilities of
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
# Import AdaBoostClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder

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
