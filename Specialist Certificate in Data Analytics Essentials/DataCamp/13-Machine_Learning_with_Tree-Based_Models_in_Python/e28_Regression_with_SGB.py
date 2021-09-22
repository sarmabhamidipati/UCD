"""
Regression with SGB
In the following set of exercises, you'll solve this bike count regression problem using stochastic gradient boosting.
Instructions
100 XP

    Instantiate a Stochastic Gradient Boosting Regressor (SGBR) and set:

        max_depth to 4 and n_estimators to 200,

        subsample to 0.9, and

        max_features to 0.75.

"""
# Import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE


df = pd.read_csv('bikes.csv')
df = df.dropna()


X = df.drop('cnt', axis=1)
y = df['cnt']

# Set seed for reproducibility
SEED = 1

# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)


# Instantiate sgbr
sgbr = GradientBoostingRegressor(max_depth=4,
                                 subsample=0.9,
                                 max_features=0.75,
                                 n_estimators=200,
                                 random_state=2)

# Fit sgbr to the training set
sgbr.fit(X_train, y_train)

# Predict test set labels
y_pred = sgbr.predict(X_test)
