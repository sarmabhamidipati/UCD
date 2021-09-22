"""
Experimenting with wider networks
Now you know everything you need to begin experimenting with different models!

A model called model_1 has been pre-loaded. You can see a summary of this model printed in the IPython Shell.
This is a relatively small network, with only 10 units in each hidden layer.

In this exercise you'll create a new model called model_2 which is similar to model_1,
except it has 100 units in each hidden layer.

After you create model_2, both models will be fitted, and a graph showing both models loss score at each
epoch will be shown. We added the argument verbose=False in the fitting commands to print out fewer updates,
since you will look at these graphically instead of as text.

Because you are fitting two models, it will take a moment to see the outputs after you hit run, so be patient.

Instructions
100 XP

    Create model_2 to replicate model_1, but use 100 nodes instead of 10 for the first two Dense layers you add with
    the 'relu' activation. Use 2 nodes for the Dense output layer with 'softmax' as the activation.
    Compile model_2 as you have done with previous models: Using 'adam' as the optimizer, 'categorical_crossentropy'
    for the loss, and metrics=['accuracy'].
    Hit 'Submit Answer' to fit both the models and visualize which one gives better results! Notice the keyword
    argument verbose=False in model.fit(): This prints out fewer updates, since you'll be evaluating the models
    graphically instead of through text.

"""
import get_new_model
import predictors
import pandas as pd
# Import the SGD optimizer
from tensorflow.keras.optimizers import SGD
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from keras.models import Sequential
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

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
model.add(Dense(100, activation='relu', input_shape=input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# Fit the model
model.fit(predictors, target, validation_split=0.3, epochs=30, callbacks=[early_stopping_monitor])


# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# Create the new model: model_2
model_2 = Sequential()


# Add the first and second layers
model_2.add(Dense(100, activation='relu', input_shape=input_shape))
model_2.add(Dense(100, activation='relu'))

# Add the output layer
model_2.add(Dense(2, activation='softmax'))

# Compile model_2
model_2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit model_1
model_1_training = model.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)

# Fit model_2
model_2_training = model_2.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)

# Create the plot
plt.plot(model_1_training.history['val_loss'], 'r', model_2_training.history['val_loss'], 'b')
plt.xlabel('Epochs')
plt.ylabel('Validation score')
plt.show()
