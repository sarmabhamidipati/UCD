"""
Making multiple updates to weights
Instructions
100 XP

    Using a for loop to iteratively update weights:
        Calculate the slope using the get_slope() function.
        Update the weights using a learning rate of 0.01.
        Calculate the mean squared error (mse) with the updated weights using the get_mse() function.
        Append mse to mse_hist.
    Hit 'Submit Answer' to visualize mse_hist. What trend do you notice?

"""
import numpy as np
import matplotlib.pyplot as plt

weights = np.array([0, 2, 1])

input_data = np.array([1, 2, 3])

target = 0

def get_error(input_data, target, weights):
    preds = (weights * input_data).sum()
    error = preds - target
    return (error)


def get_slope(input_data, target, weights):
    error = get_error(input_data, target, weights)
    slope = 2 * input_data * error
    return (slope)

def get_mse(input_data, target, weights):
    errors = get_error(input_data, target, weights)
    mse = np.mean(errors**2)
    return(mse)


n_updates = 20
mse_hist = []

# Iterate over the number of updates
for i in range(n_updates):
    # Calculate the slope: slope
    slope = get_slope(input_data, target, weights)

    # Update the weights: weights
    weights = weights - (0.01 * slope)

    # Calculate mse with new weights: mse
    mse = get_mse(input_data, target, weights)

    # Append the mse to mse_hist
    mse_hist.append(mse)

# Plot the mse history
plt.plot(mse_hist)
plt.xlabel('Iterations')
plt.ylabel('Mean Squared Error')
plt.show()