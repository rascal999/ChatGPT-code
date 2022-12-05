#!/usr/bin/env python3

import numpy as np

class NeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size):
    self.input_size = input_size
    self.hidden_size = hidden_size
    self.output_size = output_size

    # initialize weights
    self.W1 = np.random.randn(self.input_size, self.hidden_size)
    self.W2 = np.random.randn(self.hidden_size, self.output_size)

  def forward(self, input):
    # forward propagation
    self.Z1 = np.dot(input, self.W1)
    self.A1 = self.sigmoid(self.Z1)
    self.Z2 = np.dot(self.A1, self.W2)
    output = self.sigmoid(self.Z2)
    return output

  def sigmoid(self, x):
    # sigmoid activation function
    return 1/(1 + np.exp(-x))

# initialize network
nn = NeuralNetwork(2, 10, 1)

# input data
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# expected output
y = np.array([[0], [1], [1], [0]])

# predict output
output = nn.forward(x)
print(output)
