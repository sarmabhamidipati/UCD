"""
Evaluating model accuracy on validation dataset
Now it's your turn to monitor model accuracy with a validation data set. A model definition has been provided as model.
Your job is to add the code to compile it and then fit it. You'll check the validation score in each epoch.

Instructions
100 XP

    Compile your model using 'adam' as the optimizer and 'categorical_crossentropy' for the loss.
    To see what fraction of predictions are correct (the accuracy) in each epoch, specify the additional
    keyword argument metrics=['accuracy'] in model.compile().
    Fit the model using the predictors and target. Create a validation split of 30% (or 0.3).
    This will be reported in each epoch.

"""
import get_new_model
import predictors
import pandas as pd
# Import the SGD optimizer
from tensorflow.keras.optimizers import SGD
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from keras.models import Sequential


# Create list of learning rates: lr_to_test
lr_to_test = [.000001, 0.01, 1]
input_shape = (10,)

predictors = predictors.predictors

df = pd.read_csv('titanic_all_numeric.csv')

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Loop over learning rates
for lr in lr_to_test:
    print('\n\nTesting model with learning rate: %f\n' % lr)

    # Build new model to test, unaffected by previous models
    model = get_new_model.get_new_model()

    # Create SGD optimizer with specified learning rate: my_optimizer
    my_optimizer = SGD(lr=lr)

    # Compile the model
    model.compile(optimizer=my_optimizer, loss='categorical_crossentropy')

    # Fit the model
    model.fit(predictors, target)

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['accuracy'])

# Fit the model
hist = model.fit(predictors, target, validation_split=0.3)
