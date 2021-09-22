"""
Building your own digit recognition model

You've reached the final exercise of the course - you now know everything you need to build an accurate model to
recognize handwritten digits!

We've already done the basic manipulation of the MNIST dataset shown in the video, so you have X and y loaded and
ready to model with. Sequential and Dense from keras are also pre-imported.
Instructions
100 XP

    Create a Sequential object to start your model. Call this model.
    Add the first Dense hidden layer of 50 units to your model with 'relu' activation.
    For this data, the input_shape is (784,).
    Add a second Dense hidden layer with 50 units and a 'relu' activation function.
    Add the output layer. Your activation function should be 'softm
    ax', and the number of nodes in this layer should be the same as the number of possible outputs in this case: 10.
    Compile model as you have done with previous models: Using 'adam' as the optimizer,
    'categorical_crossentropy' for the loss, and metrics=['accuracy'].
    Fit the model using X and y using a validation_split of 0.3.

"""

import numpy as np
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


X = np.array([[0., 0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 0., 0.]])

y = np.array([[0., 0., 0., 0., 0., 0.],
              [0., 1., 0., 0., 0., 0.],
              [0., 0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 0., 0.],
              [0., 0., 0., 0., 1., 0.],
              [0., 1., 0., 0., 0., 0.]])


# Create the model: model
model = Sequential()

input_shape = (6,)

# Add the first hidden layer
model.add(Dense(50, activation='relu', input_shape=input_shape))


# Add the second hidden layer
model.add(Dense(50, activation='relu'))


# Add the output layer
model.add(Dense(6, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X, y, validation_split=0.3)

