"""
Compiling the model
In this exercise, you'll use the Adam optimizer and the mean squared error loss function. Go for it!
Instructions
100 XP

    Compile the model using model.compile(). Your optimizer should be 'adam'
    and the loss should be 'mean_squared_error'.
"""
import numpy as np
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential


predictors = np.array([[0, 8, 21, 35, 1, 1, 0, 1, 0],
                       [0, 9, 42, 57, 1, 1, 0, 1, 0],
                       [0, 12, 1, 19, 0, 0, 0, 1, 0],
                       [0, 12, 4, 22, 0, 0, 0, 0, 0],
                       [0, 12, 17, 35, 0, 1, 0, 0, 0],
                       [1, 13, 9, 28, 0, 0, 0, 0, 0],
                       [0, 10, 27, 43, 0, 0, 1, 0, 0],
                       [0, 12, 9, 27, 0, 0, 0, 0, 0],
                       [0, 16, 11, 33, 0, 1, 0, 1, 0],
                       [0, 12, 9, 27, 0, 0, 0, 0, 0],
                       [1, 12, 17, 35, 0, 1, 0, 0, 0],
                       [1, 12, 19, 37, 0, 0, 0, 1, 0],
                       [0, 8, 27, 41, 0, 1, 1, 0, 0],
                       [1, 9, 30, 45, 0, 0, 1, 0, 0],
                       [0, 9, 29, 44, 0, 1, 1, 0, 0],
                       [0, 12, 37, 55, 0, 1, 0, 0, 1],
                       [0, 7, 44, 57, 0, 1, 1, 0, 0],
                       [1, 12, 26, 44, 0, 1, 0, 1, 0],
                       [0, 11, 16, 33, 0, 0, 0, 0, 0],
                       [0, 12, 33, 51, 0, 1, 0, 0, 0],
                       [1, 12, 16, 34, 1, 1, 0, 1, 0],
                       [1, 7, 42, 55, 0, 1, 0, 1, 0],
                       [0, 12, 9, 27, 0, 0, 0, 0, 0],
                       [0, 11, 14, 31, 0, 1, 1, 0, 0],
                       [0, 12, 23, 41, 0, 1, 0, 0, 0],
                       [0, 6, 45, 57, 0, 1, 1, 1, 0],
                       [0, 12, 8, 26, 0, 1, 0, 1, 0],
                       [0, 10, 30, 46, 0, 1, 0, 0, 0],
                       [0, 12, 8, 26, 1, 1, 0, 1, 0],
                       [0, 12, 8, 26, 0, 1, 0, 0, 0],
                       [0, 14, 13, 33, 0, 0, 0, 0, 0],
                       [0, 12, 46, 64, 1, 0, 1, 0, 0],
                       [0, 8, 19, 33, 0, 1, 0, 0, 0],
                       [0, 17, 1, 24, 1, 0, 1, 0, 0],
                       [0, 12, 19, 37, 0, 0, 0, 1, 0],
                       [0, 12, 36, 54, 0, 0, 0, 0, 0],
                       [0, 12, 20, 38, 0, 1, 1, 0, 1],
                       [1, 12, 35, 53, 0, 1, 0, 0, 1],
                       [0, 12, 3, 21, 0, 0, 0, 0, 0],
                       [0, 14, 10, 30, 0, 1, 1, 1, 0],
                       [0, 12, 0, 18, 0, 0, 0, 0, 0],
                       [1, 14, 14, 34, 0, 1, 1, 1, 0],
                       [0, 12, 14, 32, 0, 1, 0, 1, 0],
                       [0, 9, 16, 31, 1, 1, 0, 1, 0],
                       [0, 13, 8, 27, 0, 0, 1, 0, 1],
                       [0, 7, 15, 28, 1, 1, 1, 1, 0],
                       [0, 16, 12, 34, 0, 1, 0, 1, 0],
                       [0, 10, 13, 29, 0, 0, 1, 0, 0],
                       [1, 8, 33, 47, 0, 1, 0, 0, 0],
                       [0, 12, 9, 27, 0, 1, 0, 1, 0],
                       [0, 12, 7, 25, 0, 1, 0, 0, 0],
                       [1, 16, 13, 35, 0, 1, 0, 1, 0],
                       [0, 12, 7, 25, 1, 1, 0, 1, 0],
                       [0, 12, 16, 34, 1, 1, 0, 1, 0],
                       [0, 13, 0, 19, 0, 0, 0, 0, 0],
                       [0, 12, 11, 29, 1, 0, 0, 1, 0],
                       [0, 13, 17, 36, 0, 0, 0, 1, 0],
                       [0, 10, 13, 29, 0, 1, 0, 1, 0],
                       [1, 12, 22, 40, 0, 0, 0, 1, 0],
                       [0, 12, 28, 46, 1, 1, 0, 1, 0],
                       [0, 11, 17, 34, 0, 0, 0, 0, 0],
                       [1, 12, 24, 42, 0, 1, 0, 0, 1],
                       [0, 3, 55, 64, 0, 1, 1, 1, 0],
                       [0, 12, 3, 21, 0, 0, 1, 0, 1],
                       [1, 12, 6, 24, 0, 0, 0, 1, 0],
                       [0, 10, 27, 43, 0, 1, 0, 0, 1],
                       [1, 12, 19, 37, 0, 1, 1, 1, 0],
                       [1, 12, 19, 37, 0, 1, 0, 0, 1],
                       [0, 12, 38, 56, 1, 1, 0, 1, 0],
                       [1, 10, 41, 57, 0, 1, 1, 1, 0],
                       [0, 11, 3, 20, 0, 0, 1, 1, 0],
                       [1, 14, 20, 40, 0, 1, 0, 0, 0],
                       [0, 10, 15, 31, 0, 1, 0, 0, 0],
                       [0, 8, 8, 22, 0, 1, 1, 1, 0],
                       [0, 8, 39, 53, 1, 1, 1, 1, 0],
                       [1, 6, 43, 55, 1, 1, 0, 1, 0],
                       [1, 11, 25, 42, 1, 1, 1, 1, 0],
                       [1, 12, 11, 29, 0, 1, 0, 0, 0],
                       [0, 12, 12, 30, 0, 1, 0, 0, 0],
                       [1, 12, 35, 53, 0, 1, 1, 1, 0],
                       [0, 14, 14, 34, 0, 0, 0, 0, 0],
                       [1, 12, 16, 34, 0, 1, 0, 0, 0],
                       [1, 10, 44, 60, 1, 0, 0, 1, 0],
                       [0, 16, 13, 35, 1, 0, 1, 0, 0],
                       [1, 13, 8, 27, 0, 0, 0, 1, 0],
                       [0, 12, 13, 31, 0, 0, 0, 1, 0],
                       [1, 11, 18, 35, 0, 1, 0, 0, 0],
                       [0, 12, 18, 36, 1, 1, 0, 0, 0],
                       [0, 12, 6, 24, 1, 0, 1, 0, 0],
                       [1, 11, 37, 54, 0, 1, 1, 1, 0],
                       [0, 12, 2, 20, 0, 1, 1, 1, 0],
                       [0, 12, 23, 41, 0, 1, 0, 1, 0],
                       [0, 12, 1, 19, 0, 0, 0, 0, 0],
                       [0, 12, 10, 28, 1, 1, 1, 1, 0],
                       [0, 12, 23, 41, 0, 1, 0, 1, 0],
                       [1, 12, 8, 26, 0, 1, 0, 0, 0],
                       [0, 15, 9, 30, 1, 1, 0, 1, 0],
                       [1, 12, 33, 51, 0, 1, 0, 0, 1],
                       [0, 12, 19, 37, 1, 1, 0, 1, 0],
                       [0, 13, 14, 33, 0, 1, 0, 0, 0],
                       [1, 11, 13, 30, 0, 1, 0, 0, 0],
                       [0, 10, 12, 28, 0, 1, 0, 0, 1],
                       [0, 12, 8, 26, 0, 0, 0, 0, 0],
                       [0, 12, 23, 41, 0, 1, 0, 1, 0],
                       [0, 14, 13, 33, 1, 0, 0, 1, 0],
                       [0, 12, 9, 27, 0, 1, 1, 0, 0],
                       [1, 14, 21, 41, 0, 1, 0, 0, 0],
                       [0, 5, 44, 55, 0, 1, 1, 0, 1],
                       [1, 12, 4, 22, 0, 1, 0, 0, 0],
                       [0, 8, 42, 56, 0, 1, 0, 1, 0],
                       [1, 13, 10, 29, 0, 1, 0, 0, 0],
                       [0, 12, 11, 29, 0, 0, 0, 0, 1],
                       [1, 12, 40, 58, 0, 1, 0, 0, 1],
                       [0, 12, 8, 26, 0, 0, 0, 0, 1],
                       [0, 11, 29, 46, 0, 1, 1, 0, 1],
                       [1, 16, 3, 25, 0, 0, 0, 0, 0],
                       [0, 11, 11, 28, 0, 0, 0, 0, 1],
                       [1, 12, 12, 30, 0, 1, 0, 0, 0],
                       [0, 8, 22, 36, 1, 1, 0, 0, 0],
                       [0, 12, 12, 30, 0, 1, 0, 0, 0],
                       [1, 12, 7, 25, 0, 1, 0, 0, 0],
                       [0, 12, 15, 33, 1, 0, 0, 1, 0],
                       [0, 12, 28, 46, 0, 1, 0, 0, 0],
                       [1, 12, 20, 38, 0, 1, 1, 1, 0],
                       [0, 12, 6, 24, 0, 0, 1, 0, 1],
                       [0, 12, 5, 23, 0, 0, 1, 1, 0],
                       [0, 9, 30, 45, 1, 1, 1, 1, 0],
                       [0, 13, 18, 37, 0, 1, 0, 0, 0],
                       [0, 12, 6, 24, 1, 1, 1, 1, 0],
                       [0, 12, 16, 34, 0, 0, 1, 0, 0],
                       [1, 12, 1, 19, 0, 0, 1, 0, 0],
                       [0, 12, 3, 21, 0, 0, 0, 1, 0],
                       [0, 12, 8, 26, 0, 1, 0, 0, 0],
                       [0, 14, 2, 22, 0, 0, 0, 1, 0],
                       [0, 9, 16, 31, 0, 0, 0, 1, 0],
                       [0, 10, 9, 25, 0, 1, 1, 0, 1],
                       [0, 12, 2, 20, 0, 0, 0, 0, 0],
                       [0, 7, 43, 56, 0, 1, 1, 1, 0],
                       [0, 9, 38, 53, 0, 1, 0, 1, 0],
                       [0, 12, 9, 27, 0, 1, 0, 0, 0],
                       [0, 12, 12, 30, 0, 1, 1, 0, 0],
                       [0, 12, 18, 36, 0, 1, 0, 1, 0],
                       [1, 11, 15, 32, 0, 0, 0, 1, 0],
                       [1, 11, 28, 45, 0, 1, 1, 0, 1],
                       [1, 10, 27, 43, 0, 1, 1, 0, 1],
                       [0, 12, 38, 56, 0, 1, 1, 0, 0],
                       [0, 12, 3, 21, 1, 0, 0, 1, 0],
                       [1, 12, 41, 59, 0, 1, 0, 0, 0],
                       [1, 12, 16, 34, 0, 1, 1, 0, 0],
                       [0, 13, 7, 26, 0, 1, 1, 1, 0],
                       [0, 6, 33, 45, 1, 0, 1, 1, 0],
                       [0, 14, 25, 45, 0, 1, 0, 1, 0],
                       [0, 12, 5, 23, 0, 1, 1, 0, 0],
                       [0, 14, 17, 37, 0, 0, 1, 0, 0],
                       [0, 12, 1, 19, 0, 0, 1, 0, 0],
                       [0, 12, 13, 31, 0, 1, 0, 1, 0],
                       [0, 16, 18, 40, 0, 1, 0, 0, 0],
                       [0, 14, 21, 41, 0, 1, 1, 0, 0],
                       [0, 14, 2, 22, 0, 0, 0, 0, 0],
                       [0, 12, 4, 22, 1, 0, 1, 0, 0],
                       [0, 12, 30, 48, 1, 1, 1, 0, 0],
                       [0, 13, 32, 51, 0, 0, 0, 0, 0],
                       [0, 17, 13, 36, 1, 1, 0, 0, 0],
                       [0, 12, 17, 35, 0, 0, 0, 0, 0],
                       [0, 14, 26, 46, 1, 1, 0, 0, 0],
                       [0, 16, 9, 31, 0, 0, 0, 0, 0],
                       [0, 16, 8, 30, 0, 0, 0, 0, 0],
                       [1, 15, 1, 22, 0, 1, 0, 0, 0],
                       [0, 17, 32, 55, 0, 1, 1, 0, 0],
                       [0, 12, 24, 42, 1, 1, 0, 0, 0],
                       [0, 14, 1, 21, 1, 0, 0, 0, 0],
                       [0, 12, 42, 60, 0, 1, 0, 1, 0],
                       [0, 16, 3, 25, 1, 0, 0, 1, 0],
                       [0, 12, 32, 50, 1, 1, 0, 0, 0],
                       [0, 14, 22, 42, 0, 0, 0, 0, 0],
                       [0, 16, 18, 40, 0, 1, 0, 0, 0],
                       [0, 18, 19, 43, 1, 1, 0, 0, 0],
                       [0, 15, 12, 33, 0, 1, 0, 0, 0],
                       [0, 12, 42, 60, 1, 1, 0, 0, 0],
                       [0, 12, 34, 52, 0, 1, 1, 0, 0],
                       [0, 18, 29, 53, 0, 1, 0, 0, 0],
                       [0, 16, 8, 30, 0, 0, 1, 0, 0],
                       [0, 18, 13, 37, 0, 0, 0, 1, 0],
                       [0, 16, 10, 32, 0, 0, 0, 0, 0],
                       [0, 16, 22, 44, 0, 1, 0, 0, 0],
                       [0, 16, 10, 32, 0, 1, 1, 0, 0],
                       [0, 17, 15, 38, 1, 1, 0, 0, 0],
                       [0, 12, 26, 44, 0, 1, 0, 0, 0],
                       [0, 14, 16, 36, 0, 0, 0, 0, 0],
                       [0, 18, 14, 38, 1, 1, 0, 0, 0],
                       [0, 12, 38, 56, 1, 1, 0, 0, 0],
                       [0, 12, 14, 32, 0, 1, 1, 0, 0],
                       [0, 12, 7, 25, 1, 1, 0, 0, 0],
                       [0, 18, 13, 37, 1, 0, 1, 0, 0],
                       [0, 10, 20, 36, 0, 1, 0, 0, 0],
                       [1, 16, 7, 29, 0, 1, 0, 0, 0],
                       [0, 16, 26, 48, 1, 1, 0, 0, 0],
                       [0, 16, 14, 36, 0, 1, 0, 0, 0],
                       [0, 13, 36, 55, 0, 0, 0, 0, 0],
                       [0, 12, 24, 42, 0, 1, 0, 0, 0],
                       [0, 14, 41, 61, 0, 1, 1, 0, 0],
                       [0, 16, 7, 29, 0, 1, 0, 0, 0],
                       [0, 17, 14, 37, 0, 0, 1, 0, 0],
                       [0, 12, 1, 19, 1, 0, 1, 0, 0],
                       [0, 16, 6, 28, 1, 1, 0, 1, 0],
                       [0, 12, 3, 21, 1, 1, 0, 0, 0],
                       [0, 15, 31, 52, 0, 1, 0, 0, 0],
                       [0, 13, 14, 33, 1, 1, 0, 1, 0],
                       [0, 14, 13, 33, 1, 1, 0, 0, 0],
                       [1, 16, 26, 48, 0, 1, 0, 1, 0],
                       [0, 18, 14, 38, 0, 1, 0, 0, 0],
                       [0, 13, 33, 52, 1, 1, 0, 0, 0],
                       [0, 12, 16, 34, 0, 1, 0, 0, 0],
                       [0, 18, 10, 34, 0, 1, 0, 0, 0],
                       [0, 14, 22, 42, 0, 0, 0, 0, 0],
                       [0, 14, 2, 22, 0, 0, 0, 0, 0],
                       [0, 12, 29, 47, 1, 1, 1, 0, 0],
                       [0, 12, 43, 61, 0, 1, 0, 1, 0],
                       [0, 12, 5, 23, 1, 1, 0, 0, 0],
                       [0, 16, 14, 36, 1, 1, 1, 0, 0],
                       [0, 12, 28, 46, 0, 1, 1, 0, 0],
                       [0, 11, 25, 42, 1, 1, 1, 0, 0],
                       [0, 12, 45, 63, 1, 1, 0, 0, 0],
                       [0, 14, 5, 25, 0, 0, 1, 0, 0],
                       [0, 12, 20, 38, 0, 1, 1, 1, 0],
                       [0, 16, 6, 28, 1, 1, 0, 0, 0],
                       [0, 16, 16, 38, 0, 1, 0, 0, 0],
                       [0, 11, 33, 50, 1, 1, 0, 0, 0],
                       [0, 13, 2, 21, 1, 1, 1, 0, 0],
                       [0, 12, 10, 28, 1, 0, 1, 0, 0],
                       [0, 14, 44, 64, 0, 1, 1, 0, 0],
                       [0, 14, 6, 26, 1, 1, 1, 0, 0],
                       [0, 12, 15, 33, 1, 0, 0, 0, 0],
                       [0, 12, 5, 23, 0, 1, 0, 0, 0],
                       [0, 13, 4, 23, 1, 1, 0, 1, 0],
                       [0, 14, 14, 34, 0, 1, 0, 0, 0],
                       [0, 14, 32, 52, 1, 1, 0, 0, 0],
                       [0, 12, 14, 32, 1, 1, 0, 0, 0],
                       [0, 14, 21, 41, 0, 1, 0, 0, 0],
                       [1, 12, 43, 61, 0, 1, 0, 0, 0],
                       [0, 12, 27, 45, 1, 1, 1, 0, 0],
                       [0, 12, 4, 22, 1, 0, 0, 0, 0],
                       [0, 14, 0, 20, 0, 0, 0, 0, 0],
                       [0, 12, 32, 50, 0, 1, 1, 0, 0],
                       [0, 12, 20, 38, 0, 1, 0, 0, 0],
                       [0, 15, 4, 25, 0, 0, 1, 0, 0],
                       [0, 12, 34, 52, 0, 1, 0, 0, 0],
                       [0, 13, 5, 24, 0, 0, 0, 0, 0],
                       [0, 17, 13, 36, 0, 1, 0, 1, 0],
                       [0, 14, 17, 37, 1, 1, 0, 0, 0],
                       [0, 13, 10, 29, 1, 1, 1, 0, 0],
                       [0, 16, 7, 29, 1, 1, 0, 0, 0],
                       [0, 12, 25, 43, 1, 0, 0, 0, 0],
                       [0, 12, 18, 36, 1, 1, 0, 0, 0],
                       [0, 16, 27, 49, 1, 1, 0, 1, 0],
                       [0, 16, 2, 24, 1, 0, 0, 0, 0],
                       [0, 13, 13, 32, 0, 1, 0, 0, 0],
                       [0, 14, 24, 44, 1, 0, 0, 0, 0],
                       [0, 18, 13, 37, 1, 1, 1, 0, 0],
                       [1, 14, 15, 35, 1, 0, 0, 0, 0],
                       [0, 12, 12, 30, 1, 0, 1, 0, 0],
                       [0, 12, 24, 42, 1, 1, 0, 0, 0],
                       [0, 12, 43, 61, 1, 1, 0, 0, 1],
                       [0, 12, 13, 31, 1, 1, 0, 1, 0],
                       [0, 12, 16, 34, 1, 1, 1, 0, 0],
                       [0, 11, 24, 41, 1, 1, 0, 0, 0],
                       [0, 16, 4, 26, 1, 1, 1, 0, 0],
                       [0, 12, 24, 42, 1, 1, 0, 0, 0],
                       [0, 12, 45, 63, 1, 1, 0, 0, 0],
                       [1, 12, 20, 38, 0, 1, 0, 0, 0],
                       [0, 12, 38, 56, 1, 1, 0, 0, 0],
                       [0, 18, 10, 34, 0, 1, 1, 0, 0],
                       [0, 11, 16, 33, 1, 1, 0, 0, 0],
                       [0, 12, 32, 50, 1, 1, 1, 0, 0],
                       [0, 16, 2, 24, 1, 0, 1, 0, 0],
                       [0, 13, 28, 47, 1, 0, 1, 0, 0],
                       [0, 16, 3, 25, 0, 0, 0, 0, 0],
                       [1, 13, 8, 27, 1, 0, 0, 0, 0],
                       [0, 12, 44, 62, 1, 1, 0, 1, 0],
                       [0, 12, 12, 30, 0, 1, 1, 0, 0],
                       [0, 12, 8, 26, 0, 1, 1, 0, 0],
                       [0, 12, 4, 22, 1, 1, 0, 0, 0],
                       [0, 12, 28, 46, 1, 1, 1, 0, 0],
                       [0, 13, 0, 19, 1, 0, 1, 0, 0],
                       [0, 14, 1, 21, 0, 0, 1, 0, 0],
                       [0, 14, 12, 32, 1, 1, 0, 1, 0],
                       [0, 12, 39, 57, 1, 1, 0, 0, 0],
                       [0, 12, 24, 42, 1, 1, 0, 0, 0],
                       [0, 17, 32, 55, 1, 1, 0, 0, 0],
                       [0, 16, 4, 26, 0, 0, 0, 0, 0],
                       [0, 12, 25, 43, 1, 0, 0, 0, 0],
                       [0, 12, 8, 26, 0, 0, 0, 0, 0],
                       [0, 13, 16, 35, 1, 1, 0, 0, 0],
                       [0, 12, 5, 23, 0, 0, 1, 0, 0],
                       [0, 13, 31, 50, 0, 0, 0, 0, 0],
                       [0, 12, 25, 43, 1, 0, 0, 0, 0],
                       [0, 12, 15, 33, 1, 1, 0, 0, 0],
                       [0, 14, 15, 35, 1, 1, 1, 0, 0],
                       [0, 12, 0, 18, 1, 0, 0, 0, 0],
                       [0, 12, 19, 37, 0, 1, 0, 0, 0],
                       [0, 12, 21, 39, 1, 0, 0, 0, 0],
                       [0, 12, 6, 24, 1, 0, 0, 0, 0],
                       [1, 12, 14, 32, 1, 1, 0, 0, 0],
                       [0, 13, 30, 49, 1, 1, 0, 0, 0],
                       [0, 12, 8, 26, 1, 0, 0, 0, 0],
                       [1, 9, 33, 48, 0, 0, 0, 0, 0],
                       [0, 13, 16, 35, 0, 0, 0, 0, 0],
                       [0, 12, 20, 38, 1, 0, 1, 0, 0],
                       [0, 13, 6, 25, 1, 1, 1, 0, 0],
                       [1, 12, 10, 28, 1, 1, 0, 0, 0],
                       [0, 13, 1, 20, 1, 0, 1, 0, 0],
                       [0, 12, 2, 20, 0, 0, 1, 0, 0],
                       [0, 13, 0, 19, 1, 0, 1, 0, 0],
                       [0, 16, 17, 39, 0, 1, 0, 0, 0],
                       [0, 12, 8, 26, 1, 0, 0, 0, 0],
                       [0, 12, 4, 22, 0, 0, 1, 0, 0],
                       [0, 12, 15, 33, 1, 0, 0, 0, 0],
                       [0, 12, 29, 47, 1, 1, 0, 0, 0],
                       [0, 12, 23, 41, 1, 1, 1, 0, 0],
                       [0, 12, 39, 57, 1, 1, 1, 0, 0],
                       [0, 12, 14, 32, 1, 1, 1, 0, 0],
                       [0, 17, 6, 29, 1, 0, 1, 0, 0],
                       [1, 14, 12, 32, 0, 1, 1, 0, 0],
                       [0, 12, 26, 44, 1, 0, 1, 0, 0],
                       [0, 14, 32, 52, 1, 1, 0, 0, 0],
                       [0, 15, 6, 27, 1, 1, 0, 0, 0],
                       [0, 12, 40, 58, 1, 1, 0, 0, 0],
                       [0, 12, 18, 36, 1, 1, 0, 1, 0],
                       [0, 11, 12, 29, 1, 0, 0, 0, 0],
                       [0, 12, 36, 54, 1, 1, 1, 0, 1],
                       [0, 12, 19, 37, 1, 1, 0, 0, 0],
                       [0, 16, 42, 64, 1, 0, 0, 1, 0],
                       [0, 13, 2, 21, 1, 1, 0, 0, 0],
                       [0, 12, 33, 51, 1, 1, 0, 0, 0],
                       [0, 12, 14, 32, 1, 1, 1, 0, 0],
                       [0, 12, 22, 40, 0, 0, 0, 0, 0],
                       [0, 12, 20, 38, 1, 1, 0, 0, 0],
                       [0, 12, 15, 33, 1, 1, 0, 0, 0],
                       [0, 12, 35, 53, 0, 1, 0, 0, 0],
                       [0, 12, 7, 25, 1, 1, 0, 0, 0],
                       [0, 12, 45, 63, 1, 0, 0, 1, 0],
                       [0, 12, 9, 27, 1, 0, 0, 0, 0],
                       [0, 12, 2, 20, 1, 1, 1, 0, 0],
                       [0, 17, 3, 26, 0, 0, 1, 0, 0],
                       [1, 14, 19, 39, 1, 1, 0, 0, 0],
                       [0, 12, 14, 32, 1, 1, 1, 0, 0],
                       [0, 4, 54, 64, 0, 1, 0, 0, 0],
                       [0, 14, 17, 37, 0, 1, 0, 0, 0],
                       [0, 8, 29, 43, 1, 1, 0, 0, 0],
                       [0, 15, 26, 47, 1, 0, 1, 0, 0],
                       [0, 2, 16, 24, 0, 0, 0, 0, 0],
                       [0, 8, 29, 43, 1, 0, 0, 0, 0],
                       [0, 11, 20, 37, 1, 1, 0, 0, 0],
                       [0, 10, 38, 54, 1, 1, 1, 0, 0],
                       [0, 8, 37, 51, 1, 1, 1, 0, 0],
                       [0, 9, 48, 63, 0, 0, 0, 0, 0],
                       [0, 12, 16, 34, 1, 0, 0, 0, 0],
                       [0, 8, 38, 52, 1, 1, 0, 0, 0],
                       [0, 14, 0, 20, 0, 0, 0, 0, 0],
                       [1, 12, 14, 32, 0, 0, 0, 0, 0],
                       [0, 12, 2, 20, 1, 1, 0, 0, 0],
                       [0, 16, 21, 43, 0, 1, 0, 0, 0],
                       [0, 13, 15, 34, 1, 1, 0, 0, 0],
                       [0, 16, 20, 42, 1, 0, 0, 0, 0],
                       [0, 14, 12, 32, 1, 1, 0, 0, 0],
                       [0, 12, 7, 25, 0, 0, 1, 0, 0],
                       [0, 11, 4, 21, 0, 1, 0, 0, 0],
                       [0, 13, 9, 28, 0, 1, 1, 0, 0],
                       [0, 12, 43, 61, 1, 1, 1, 0, 0],
                       [0, 10, 19, 35, 0, 0, 1, 0, 0],
                       [0, 8, 49, 63, 1, 0, 0, 0, 0],
                       [0, 12, 38, 56, 1, 1, 0, 0, 0],
                       [0, 12, 13, 31, 1, 1, 0, 0, 0],
                       [0, 12, 14, 32, 1, 1, 0, 0, 0],
                       [0, 12, 20, 38, 0, 0, 0, 0, 0],
                       [0, 12, 7, 25, 1, 0, 0, 0, 0],
                       [1, 12, 9, 27, 1, 1, 0, 1, 0],
                       [0, 12, 6, 24, 1, 0, 0, 0, 0],
                       [0, 12, 5, 23, 1, 1, 1, 0, 0],
                       [0, 13, 1, 20, 1, 0, 1, 0, 0],
                       [1, 14, 22, 42, 0, 1, 0, 0, 0],
                       [0, 12, 24, 42, 1, 1, 0, 0, 0],
                       [1, 12, 15, 33, 1, 0, 0, 0, 0],
                       [0, 11, 8, 25, 1, 1, 1, 0, 0],
                       [0, 11, 17, 34, 1, 1, 1, 0, 0],
                       [0, 12, 2, 20, 0, 0, 1, 0, 0],
                       [0, 12, 20, 38, 0, 1, 1, 0, 0],
                       [1, 12, 26, 44, 0, 1, 0, 0, 0],
                       [0, 10, 37, 53, 1, 1, 1, 0, 0],
                       [0, 12, 41, 59, 1, 0, 0, 0, 0],
                       [0, 12, 27, 45, 1, 1, 0, 0, 0],
                       [1, 12, 5, 23, 1, 1, 0, 0, 0],
                       [0, 14, 16, 36, 0, 1, 0, 0, 0],
                       [0, 14, 19, 39, 1, 1, 0, 0, 0],
                       [0, 12, 10, 28, 0, 1, 0, 0, 0],
                       [1, 13, 1, 20, 0, 0, 1, 0, 0],
                       [1, 12, 43, 61, 1, 1, 0, 0, 0],
                       [0, 13, 3, 22, 0, 0, 0, 0, 0],
                       [0, 12, 0, 18, 1, 0, 0, 0, 0],
                       [0, 12, 26, 44, 1, 1, 1, 0, 0],
                       [1, 10, 25, 41, 1, 1, 0, 0, 0],
                       [0, 12, 15, 33, 1, 1, 0, 0, 0],
                       [0, 14, 10, 30, 1, 0, 1, 0, 0],
                       [1, 11, 45, 62, 1, 0, 0, 0, 0],
                       [0, 11, 3, 20, 0, 0, 0, 0, 0],
                       [1, 8, 47, 61, 0, 1, 0, 0, 0],
                       [0, 16, 6, 28, 1, 1, 0, 0, 0],
                       [0, 10, 33, 49, 1, 0, 1, 0, 0],
                       [0, 16, 3, 25, 0, 0, 0, 1, 0],
                       [1, 14, 4, 24, 0, 0, 0, 0, 0],
                       [1, 14, 34, 54, 0, 1, 0, 0, 0],
                       [0, 11, 39, 56, 0, 1, 1, 0, 0],
                       [0, 12, 17, 35, 1, 1, 1, 0, 0],
                       [1, 9, 47, 62, 0, 1, 0, 0, 0],
                       [0, 11, 2, 19, 0, 0, 0, 0, 0],
                       [0, 13, 0, 19, 0, 0, 1, 0, 0],
                       [0, 14, 24, 44, 1, 0, 0, 0, 0],
                       [1, 12, 25, 43, 0, 1, 0, 0, 0],
                       [0, 14, 6, 26, 1, 0, 0, 0, 0],
                       [0, 12, 10, 28, 1, 0, 0, 0, 0],
                       [0, 12, 33, 51, 1, 1, 0, 0, 0],
                       [0, 12, 12, 30, 0, 0, 0, 0, 0],
                       [0, 12, 9, 27, 1, 1, 1, 0, 0],
                       [1, 11, 18, 35, 0, 1, 1, 0, 0],
                       [0, 12, 10, 28, 0, 1, 0, 0, 0],
                       [0, 8, 45, 59, 1, 0, 1, 0, 0],
                       [1, 9, 46, 61, 1, 1, 0, 0, 0],
                       [0, 7, 14, 27, 0, 1, 1, 0, 0],
                       [0, 11, 36, 53, 1, 0, 0, 0, 0],
                       [1, 13, 34, 53, 0, 1, 0, 0, 1],
                       [0, 18, 15, 39, 0, 1, 0, 0, 0],
                       [0, 17, 31, 54, 0, 1, 0, 1, 0],
                       [0, 16, 6, 28, 1, 0, 0, 1, 0],
                       [0, 14, 15, 35, 0, 1, 1, 0, 0],
                       [0, 12, 30, 48, 0, 1, 0, 0, 0],
                       [0, 18, 8, 32, 0, 1, 0, 0, 0],
                       [0, 18, 5, 29, 0, 1, 0, 1, 0],
                       [1, 17, 3, 26, 1, 0, 0, 0, 0],
                       [0, 13, 17, 36, 0, 1, 1, 0, 0],
                       [1, 16, 5, 27, 0, 1, 0, 1, 0],
                       [0, 14, 10, 30, 1, 1, 0, 0, 0],
                       [0, 15, 33, 54, 1, 0, 0, 0, 0],
                       [0, 18, 3, 27, 0, 1, 0, 0, 0],
                       [0, 16, 0, 18, 1, 0, 0, 0, 0],
                       [0, 16, 13, 35, 0, 1, 1, 0, 0],
                       [0, 18, 12, 36, 0, 1, 0, 0, 0],
                       [0, 16, 6, 28, 1, 1, 0, 0, 0],
                       [0, 17, 7, 30, 0, 1, 0, 0, 0],
                       [1, 16, 14, 36, 0, 1, 1, 0, 0],
                       [0, 17, 5, 28, 1, 0, 0, 0, 0],
                       [0, 15, 10, 31, 1, 1, 1, 0, 0],
                       [0, 18, 11, 35, 1, 1, 0, 0, 0],
                       [0, 17, 24, 47, 1, 1, 0, 0, 0],
                       [0, 16, 9, 31, 0, 0, 0, 1, 0],
                       [0, 18, 12, 36, 0, 1, 1, 0, 0],
                       [0, 18, 19, 43, 0, 1, 0, 0, 0],
                       [0, 14, 14, 34, 1, 1, 0, 0, 0],
                       [0, 16, 17, 39, 1, 0, 0, 1, 0],
                       [0, 18, 7, 31, 0, 0, 1, 0, 0],
                       [0, 18, 7, 31, 0, 1, 0, 0, 0],
                       [0, 16, 22, 44, 1, 1, 0, 0, 0],
                       [0, 12, 28, 46, 1, 1, 0, 0, 0],
                       [0, 16, 16, 38, 1, 0, 0, 0, 0],
                       [0, 16, 16, 38, 0, 0, 1, 0, 0],
                       [0, 16, 7, 29, 1, 1, 0, 0, 0],
                       [0, 12, 11, 29, 1, 0, 0, 0, 0],
                       [0, 12, 11, 29, 1, 1, 0, 0, 0],
                       [0, 12, 16, 34, 1, 0, 0, 0, 0],
                       [1, 18, 33, 57, 0, 0, 0, 0, 0],
                       [0, 12, 21, 39, 1, 1, 1, 0, 0],
                       [0, 16, 4, 26, 0, 1, 0, 1, 0],
                       [0, 15, 13, 34, 0, 1, 0, 0, 0],
                       [1, 18, 14, 38, 0, 1, 0, 0, 0],
                       [0, 16, 10, 32, 1, 1, 0, 0, 0],
                       [0, 18, 14, 38, 0, 1, 1, 0, 0],
                       [0, 16, 29, 51, 0, 1, 1, 0, 0],
                       [0, 12, 4, 22, 0, 0, 0, 0, 0],
                       [0, 18, 27, 51, 0, 1, 0, 0, 0],
                       [0, 12, 3, 21, 0, 1, 0, 0, 0],
                       [1, 16, 14, 36, 0, 1, 1, 0, 0],
                       [0, 14, 0, 20, 0, 1, 0, 0, 1],
                       [0, 18, 33, 57, 0, 1, 0, 0, 0],
                       [0, 16, 38, 60, 0, 1, 1, 0, 0],
                       [1, 18, 18, 42, 1, 1, 0, 0, 0],
                       [0, 17, 3, 26, 0, 0, 0, 1, 0],
                       [0, 18, 40, 64, 1, 0, 0, 0, 0],
                       [0, 14, 19, 39, 0, 0, 0, 1, 0],
                       [0, 14, 4, 24, 1, 0, 0, 0, 0],
                       [0, 16, 11, 33, 1, 1, 0, 0, 0],
                       [0, 16, 16, 38, 1, 1, 0, 0, 0],
                       [0, 14, 22, 42, 0, 1, 0, 0, 0],
                       [1, 17, 13, 36, 1, 0, 0, 0, 0],
                       [1, 16, 28, 50, 1, 1, 1, 0, 0],
                       [0, 16, 10, 32, 1, 1, 0, 0, 0],
                       [0, 16, 5, 27, 1, 0, 1, 0, 0],
                       [0, 15, 5, 26, 0, 0, 0, 0, 0],
                       [0, 18, 37, 61, 1, 0, 0, 1, 0],
                       [1, 17, 26, 49, 1, 1, 0, 0, 0],
                       [0, 16, 4, 26, 1, 1, 1, 0, 0],
                       [1, 18, 31, 55, 1, 0, 0, 0, 0],
                       [1, 17, 13, 36, 1, 1, 0, 0, 0],
                       [0, 12, 42, 60, 1, 1, 0, 0, 0],
                       [0, 17, 18, 41, 0, 1, 0, 0, 0],
                       [0, 12, 3, 21, 1, 1, 0, 0, 0],
                       [0, 17, 10, 33, 1, 0, 0, 0, 0],
                       [1, 16, 10, 32, 1, 0, 0, 0, 0],
                       [0, 16, 17, 39, 1, 1, 0, 0, 0],
                       [0, 18, 7, 31, 0, 1, 0, 0, 0],
                       [0, 16, 14, 36, 1, 1, 0, 0, 0],
                       [1, 16, 22, 44, 1, 1, 0, 0, 0],
                       [0, 17, 14, 37, 1, 1, 0, 0, 0],
                       [0, 16, 11, 33, 0, 1, 0, 0, 0],
                       [1, 18, 23, 47, 0, 1, 0, 0, 0],
                       [1, 12, 39, 57, 0, 1, 0, 0, 0],
                       [0, 16, 15, 37, 0, 1, 0, 0, 0],
                       [0, 14, 15, 35, 1, 0, 0, 0, 0],
                       [0, 16, 10, 32, 0, 0, 0, 0, 0],
                       [0, 12, 25, 43, 1, 0, 1, 0, 0],
                       [0, 14, 12, 32, 1, 1, 0, 0, 0],
                       [0, 16, 7, 29, 1, 1, 1, 0, 0],
                       [1, 17, 7, 30, 0, 1, 0, 0, 0],
                       [0, 16, 17, 39, 0, 1, 0, 1, 0],
                       [1, 16, 10, 32, 0, 1, 0, 0, 0],
                       [0, 17, 2, 25, 0, 1, 1, 0, 0],
                       [1, 9, 34, 49, 1, 1, 1, 0, 0],
                       [0, 15, 11, 32, 1, 1, 0, 0, 0],
                       [0, 15, 10, 31, 0, 0, 0, 0, 0],
                       [0, 12, 12, 30, 0, 1, 1, 0, 0],
                       [1, 16, 6, 28, 1, 0, 0, 0, 0],
                       [0, 18, 5, 29, 0, 0, 0, 0, 0],
                       [0, 12, 33, 51, 1, 1, 0, 0, 0],
                       [1, 17, 25, 48, 1, 1, 0, 0, 0],
                       [1, 12, 13, 31, 0, 1, 1, 0, 0],
                       [0, 16, 33, 55, 0, 1, 0, 1, 0]])

# Specify the model
n_cols = predictors.shape[1]
model = Sequential()
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Verify that model contains information from compiling
print("Loss function: " + model.loss)
