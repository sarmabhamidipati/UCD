"""
Improving model weights
Instructions
100 XP

    Set the learning rate to be 0.01 and calculate the error from the original predictions. This has been done for you.
    Calculate the updated weights by subtracting the product of learning_rate and slope from weights.
    Calculate the updated predictions by multiplying weights_updated with input_data and computing their sum.
    Calculate the error for the new predictions. Store the result as error_updated.
    Hit 'Submit Answer' to compare the updated error to the original!

"""

import  numpy as np

weights = np.array([0, 2, 1])

input_data = np.array([1, 2, 3])

target = 0

# Set the learning rate: learning_rate
learning_rate = 0.01

# Calculate the predictions: preds
preds = (weights * input_data).sum()

# Calculate the error: error
error = preds - target

# Calculate the slope: slope
slope = 2 * input_data * error

# Update the weights: weights_updated
weights_updated = weights - (learning_rate * slope)

# Get updated predictions: preds_updated
preds_updated = (weights_updated * input_data).sum()

# Calculate updated error: error_updated
error_updated = preds_updated - target

# Print the original error
print(error)

# Print the updated error
print(error_updated)
