inputs = [1, 2, 3, 2.5] # 3 input/neuron -> 3 weight
weights = [0.2, 0.8, -0.5, 1.0] # every unique neuron has unique bias
bias = 2



output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias
print(output)