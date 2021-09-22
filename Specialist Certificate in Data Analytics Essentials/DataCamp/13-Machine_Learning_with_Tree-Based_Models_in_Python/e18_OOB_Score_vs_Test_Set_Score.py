"""
OOB Score vs Test Set Score
Now that you instantiated bc, you will fit it to the training set and evaluate its test set and OOB accuracies.

The dataset is processed for you and split into 80% train and 20% test. The feature matrices X_train and X_test,
as well as the arrays of labels y_train and y_test are available in your workspace.
In addition, we have also loaded the classifier bc instantiated in the previous exercise and
the function accuracy_score() from sklearn.metrics.

Instructions
100 XP

    Fit bc to the training set and predict the test set labels and assign the results to y_pred.

    Evaluate the test set accuracy acc_test by calling accuracy_score.

    Evaluate bc's OOB accuracy acc_oob by extracting the attribute oob_score_ from bc.

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


# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate test set accuracy
acc_test = accuracy_score(y_test, y_pred)

# Evaluate OOB accuracy
acc_oob = bc.oob_score_

# Print acc_test and acc_oob
print('Test set accuracy: {:.3f}, OOB accuracy: {:.3f}'.format(acc_test, acc_oob))