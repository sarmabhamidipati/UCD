"""
Evaluate Bagging performance
Now that you instantiated the bagging classifier, it's time to train it and evaluate its test set accuracy.

The Indian Liver Patient dataset is processed for you and split into 80% train and 20% test.
The feature matrices X_train and X_test, as well as the arrays of labels y_train and y_test are available
in your workspace. In addition, we have also loaded the bagging classifier bc that you instantiated
in the previous exercise and the function accuracy_score() from sklearn.metrics.
Instructions
100 XP

    Fit bc to the training set.

    Predict the test set labels and assign the result to y_pred.

    Determine bc's test set accuracy.

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
#print(df.info())


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
# Instantiate a classification-tree 'dt'
dt = DecisionTreeClassifier(max_depth=4, min_samples_leaf=0.16, random_state=SEED)

# Instantiate a BaggingClassifier 'bc'
bc = BaggingClassifier(base_estimator=dt, n_estimators=300, n_jobs=-1)

# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate acc_test
acc_test = accuracy_score(y_test, y_pred)
print('Test set accuracy of bc: {:.2f}'.format(acc_test))



