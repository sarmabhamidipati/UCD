"""
Linear regression on all Anscombe data

Now, to verify that all four of the Anscombe data sets have the same slope and intercept from a linear regression,
you will compute the slope and intercept for each set. The data are stored in lists; anscombe_x = [x1, x2, x3, x4]
and anscombe_y = [y1, y2, y3, y4], where, for example, x2 and y2 are the and values for the second Anscombe data set.

Write a for loop to do the following for each Anscombe data set.

    Compute the slope and intercept.
    Print the slope and intercept.
"""
import numpy as np
import matplotlib.pyplot as plt

anscombe_x = [np.array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.]),
              np.array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.]),
              np.array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.]),
              np.array([8., 8., 8., 8., 8., 8., 8., 19., 8., 8., 8.])
              ]
anscombe_y = [np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84,
                        4.82, 5.68]),
              np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]),
              np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15,
                        6.42, 5.73]),
              np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56,
                        7.91, 6.89])]

# Iterate through x,y pairs
for x, y in zip(anscombe_x, anscombe_y):
    # Compute the slope and intercept: a, b
    a, b = np.polyfit(x, y, 1)

    # Print the result
    print('slope:', a, 'intercept:', b)
