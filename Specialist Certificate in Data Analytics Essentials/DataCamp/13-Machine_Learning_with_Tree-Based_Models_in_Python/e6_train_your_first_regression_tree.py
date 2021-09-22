"""
Train your first regression tree

"""
import import_data_for_supervised_learning1
# Import DecisionTreeRegressor from sklearn.tree
from sklearn.tree import DecisionTreeRegressor

# Instantiate dt
dt = DecisionTreeRegressor(max_depth=8,
                           min_samples_leaf=0.13,
                           random_state=3)

# Fit dt to the training set
dt.fit(import_data_for_supervised_learning1.X_train, import_data_for_supervised_learning1.y_train)
