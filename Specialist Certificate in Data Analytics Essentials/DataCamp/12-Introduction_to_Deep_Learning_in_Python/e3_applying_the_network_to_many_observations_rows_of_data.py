"""
Applying the network to many observations/rows of data
Instructions
100 XP

    Define a function called predict_with_network() that accepts two arguments - input_data_row and
    weights - and returns a prediction from the network as the output.
    Calculate the input and output values for each node, storing them as:
    node_0_input, node_0_output, node_1_input, and node_1_output.
        To calculate the input value of a node, multiply the relevant arrays together and compute their sum.
        To calculate the output value of a node, apply the relu() function to the input value of the node.
    Calculate the model output by calculating input_to_final_layer and model_output in the same way
    you calculated the input and output values for the nodes.
    Use a for loop to iterate over input_data:
        Use your predict_with_network() to generate predictions for each row of the
        input_data - input_data_row. Append each prediction to results.

"""
import numpy as np

input_data = np.array([3, 5])
weights = {'node_0': np.array([2, 4]), 'node_1': np.array([4, -5]), 'output': np.array([2, 7])}


def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(0, input)

    # Return the value just calculated
    return (output)


# Define predict_with_network()
def predict_with_network(input_data_row, weights):
    # Calculate node 0 value
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # Calculate node 1 value
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = relu(input_to_final_layer)

    # Return model output
    return (model_output)


# Create empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(predict_with_network(input_data_row, weights))

# Print results
print(results)
