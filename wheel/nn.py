import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import expit


class NeuralNetwork(object):

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.i_nodes = input_nodes
        self.h_nodes = hidden_nodes
        self.o_nodes = output_nodes
        self.lr = learning_rate

        self.ih_weights = np.random.uniform(.0, pow(self.h_nodes, -0.5), (self.h_nodes, self.i_nodes))
        self.ho_weights = np.random.uniform(.0, pow(self.o_nodes, -0.5), (self.o_nodes, self.h_nodes))

        self.activation_func = lambda x: expit(x)

    # forward propagation and back propagation
    def train(self, input_list, true_list):
        inputs = np.array(input_list, ndmin=2).T
        targets = np.array(true_list, ndmin=2).T

        hidden_inputs = np.dot(self.ih_weights, inputs)
        hidden_outputs = self.activation_func(hidden_inputs)

        final_inputs = np.dot(self.ho_weights, hidden_outputs)
        final_outputs = self.activation_func(final_inputs)

        # back propagation
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.ho_weights.T, output_errors)

        self.ho_weights += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), \
                                            np.transpose(hidden_outputs))
        self.ih_weights += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), \
                                            np.transpose(inputs))

        pass

    def query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T

        hidden_inputs = np.dot(self.ih_weights, inputs)
        hidden_outputs = self.activation_func(hidden_inputs)

        final_inputs = np.dot(self.ho_weights, hidden_outputs)
        final_outputs = self.activation_func(final_inputs)

        return final_outputs



if __name__ == '__main__':
    INPUT_NODES = 3
    HIDDEN_NODES = 3
    OUTPUT_NODES = 3
    learning_rate = 0.5

    nn = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, learning_rate)

    test_x = [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]

    test_y = [
        [1, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    nn.train(test_x, test_y)