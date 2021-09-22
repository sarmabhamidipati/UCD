"""
Scaling up to multiple data points
Instructions
100 XP

    Import mean_squared_error from sklearn.metrics.
    Using a for loop to iterate over each row of input_data:
        Make predictions for each row with weights_0 using the predict_with_network()
        function and append it to model_output_0.
        Do the same for weights_1, appending the predictions to model_output_1.
    Calculate the mean squared error of model_output_0 and then model_output_1 using the mean_squared_error() function.
    The first argument should be the actual values (target_actuals), and the
    second argument should be the predicted values (model_output_0 or model_output_1).

"""

import numpy as np
from sklearn.metrics import mean_squared_error

def relu(input):
    return (max(0, input))


input_data = [np.array([0, 3]), np.array([1, 2]), np.array([-1, -2]), np.array([4, 0])]

weights_0 = {'node_0': np.array([2, 1]), 'node_1': np.array([1, 2]), 'output': np.array([1, 1])}

weights_1 = {'node_0': np.array([2, 1]),
             'node_1': np.array([1., 1.5]),
             'output': np.array([1., 1.5])}


def predict_with_network(input_data_point, weights):
    node_0_input = (input_data_point * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    node_1_input = (input_data_point * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    hidden_layer_values = np.array([node_0_output, node_1_output])
    input_to_final_layer = (hidden_layer_values * weights['output']).sum()
    model_output = relu(input_to_final_layer)
    return (model_output)

target_actuals = [1, 3, 5, 7]


# Create model_output_0
model_output_0 = []
# Create model_output_1
model_output_1 = []

# Loop over input_data
for row in input_data:
    # Append prediction to model_output_0
    model_output_0.append(predict_with_network(row, weights_0))

    # Append prediction to model_output_1
    model_output_1.append(predict_with_network(row, weights_1))

# Calculate the mean squared error for model_output_0: mse_0
mse_0 = mean_squared_error(model_output_0, target_actuals)

# Calculate the mean squared error for model_output_1: mse_1
mse_1 = mean_squared_error(model_output_1, target_actuals)

# Print mse_0 and mse_1
print("Mean squared error with weights_0: %f" % mse_0)
print("Mean squared error with weights_1: %f" % mse_1)


