import numpy as np

inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

# output = np.dot(inputs, weights) + bias
output = np.dot(weights, inputs) + biases # -> 3*3 . 3*1 -> OW led to shape

print(output)