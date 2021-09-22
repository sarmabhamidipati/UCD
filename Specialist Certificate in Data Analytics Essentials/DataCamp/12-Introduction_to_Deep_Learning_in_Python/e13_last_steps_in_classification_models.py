"""
Last steps in classification models

"""
import pandas as pd
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
# from keras.utils import to_categorical
from keras.utils.np_utils import to_categorical
import numpy as np
import predictors

df = pd.read_csv('titanic_all_numeric.csv')

predictors = predictors.predictors

n_cols = 10

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape = (n_cols,)))

# Add the output layer
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='sgd', loss='categorical_crossentropy',
metrics=['accuracy'])

# Fit the model
model.fit(predictors, target)
