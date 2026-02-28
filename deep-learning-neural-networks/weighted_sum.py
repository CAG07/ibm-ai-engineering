import numpy as np

inputs = np.array([0.3, 0.7])    # Input value
node_weights = np.array([0.2, 0.4])    # Input value
node_bias = 0.1    # Input value

def compute_weighted_sum(inputs, node_weights, bias):
    return np.dot(inputs, node_weights) + bias

weighted_sum = compute_weighted_sum(inputs, node_weights, node_bias)
print('The weighted sum at the first node in the hidden layer is {}'.format(np.around(weighted_sum, decimals=4)))