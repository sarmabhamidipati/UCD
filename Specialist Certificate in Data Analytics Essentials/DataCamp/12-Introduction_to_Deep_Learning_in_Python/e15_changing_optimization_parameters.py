"""
Changing optimization parameters
Instructions
100 XP

    Import SGD from keras.optimizers.
    Create a list of learning rates to try optimizing with called lr_to_test.
    The learning rates in it should be .000001, 0.01, and 1.
    Using a for loop to iterate over lr_to_test:
        Use the get_new_model() function to build a new, unoptimized model.
        Create an optimizer called my_optimizer using the SGD() constructor with keyword argument lr=lr.
        Compile your model. Set the optimizer parameter to be the SGD object you created above, and
        because this is a classification problem, use 'categorical_crossentropy' for the loss parameter.
        Fit your model using the predictors and target.

"""

import get_new_model
import predictors
import pandas as pd
# Import the SGD optimizer
from tensorflow.keras.optimizers import SGD
from keras.utils.np_utils import to_categorical

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
