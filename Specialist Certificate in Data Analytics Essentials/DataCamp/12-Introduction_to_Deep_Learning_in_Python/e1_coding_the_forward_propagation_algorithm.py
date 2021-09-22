"""
Coding the forward propagation algorithm
The input data has been pre-loaded as input_data, and the weights are available in a dictionary called weights.
The array of weights for the first node in the hidden layer are in weights['node_0'], and the array of weights
for the second node in the hidden layer are in weights['node_1'].

The weights feeding into the output node are available in weights['output'].

NumPy will be pre-imported for you as np in all exercises.

Instructions
100 XP

    Calculate the value in node 0 by multiplying input_data by its weights weights['node_0'] and computing their sum.
    This is the 1st node in the hidden layer.
    Calculate the value in node 1 using input_data and weights['node_1']. This is the 2nd node in the hidden layer.
    Put the hidden layer values into an array. This has been done for you.
    Generate the prediction by multiplying hidden_layer_outputs by weights['output'] and computing their sum.
    Hit 'Submit Answer' to print the output!

"""

import numpy as np

input_data = np.array([3, 5])
weights = {'node_0': np.array([2, 4]), 'node_1': np.array([4, -5]), 'output': np.array([2, 7])}

# Calculate node 0 value: node_0_value
node_0_value = (input_data * weights['node_0']).sum()

# Calculate node 1 value: node_1_value
node_1_value = (input_data * weights['node_1']).sum()

# Put node values into array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_value, node_1_value])

# Calculate output: output
output = (hidden_layer_outputs * weights['output']).sum()

# Print output
print(output)
