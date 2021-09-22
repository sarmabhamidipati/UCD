"""
Calculating slopes

Instructions
100 XP

    Calculate the predictions, preds, by multiplying weights by the input_data and computing their sum.
    Calculate the error, which is preds minus target. Notice that this error corresponds to xb-y in the gradient expression.
    Calculate the slope of the loss function with respect to the prediction.
    To do this, you need to take the product of input_data and error and multiply that by 2.

"""

import  numpy as np

weights = np.array([0, 2, 1])

input_data = np.array([1, 2, 3])

target = 0

# Calculate the predictions: preds
preds = (weights * input_data).sum()

# Calculate the error: error
error = preds - target

# Calculate the slope: slope
slope = input_data * error * 2

# Print the slope
print(slope)
