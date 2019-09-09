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


def get_mnist_data(need_length = 1000):

    with open('data/mnist_test.csv', 'r') as f:
        mnist_y = []
        mnist_x = []
        for i in range(need_length):
            row = f.readline().split(',')
            mnist_y.append(row[0])
            mnist_x.append(row[1:])

    return mnist_x, mnist_y


def test_nn():

    #prepare data
    mnist_x, mnist_y = get_mnist_data()

    #test image and label
    label, image_arr = mnist_y[0], np.array(mnist_x[0], dtype=np.float).reshape((28, 28))

    print('label is {0}\npic show below:'.format(label))
    plt.imshow(image_arr, cmap='Greys', interpolation='None')

    #design nn scale
    INPUT_NODES = 28 * 28
    HIDDEN_NODES = 100
    OUTPUT_NODES = 10
    learning_rate = 0.2

    EPOCHS = 5

    train_size = 900
    test_size = 100

    #train
    mnist_nn = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, learning_rate)

    for epoch in range(EPOCHS):
        for i in range(train_size):
            inputs = np.array(mnist_x[i], dtype=np.float) / 255 * 0.99 + 0.01
            label = np.zeros(OUTPUT_NODES) + 0.01
            label[int(mnist_y[i])] = 0.99

            mnist_nn.train(inputs, label)

    #test score
    err = 0
    for i in range(test_size):
        target = int(mnist_y[-i])
        pred_prob = mnist_nn.query(np.array(mnist_x[-i], dtype=np.float) / 255 * 0.99 + 0.01)
        pred = np.argmax(pred_prob)

        if target != pred:
            print('true {0}, pred {1}'.format(target, pred))
            err += 1

    print('error (numbers, rate) : ({0}, {1})'.format(err, err / test_size))


#cmp sklearn knn
from sklearn.neighbors import KNeighborsClassifier


def cal_accuration(target, pred):
    err = 0
    sz = len(target)

    for idx in range(sz):
        if target[idx] != pred[idx]:
            err += 1

    return err, err / sz


def data_to_arr():
    ip_arr = []
    out_arr = []
    for i in range(train_size + test_size):
        inputs = np.array(mnist_x[i], dtype=np.double) / 255 * 0.99 + 0.01

        label = np.zeros(OUTPUT_NODES, dtype=np.double) + 0.01
        label[int(mnist_y[i])] = 0.99

        ip_arr.append(inputs)
        out_arr.append(label)

    return np.array(ip_arr), np.array(out_arr)


def cmp_skl_knn(train_X, train_y, test_X, test_y):
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(train_X, train_y)

    pred_y = model.predict(test_X)

    err, err_rate = cal_accuration(test_y, pred_y)

    print("error {0}, error rate {1}".format(err, err_rate))


##cmp pytorch
import torch


class torchNN(object):

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate=0.5, batch=64):

        self.BATCH, self.D_in, self.H, self.D_out = batch, input_nodes, hidden_nodes, output_nodes

        self.lr = learning_rate

        dtype = torch.float
        device = torch.device("cpu")

        self.w1 = torch.randn(self.D_in, self.H, device=device, dtype=torch.float64, requires_grad=True)
        self.w2 = torch.randn(self.H, self.D_out, device=device, dtype=torch.float64, requires_grad=True)

        self.activation_fuc = torch.softmax  # torch.sigmoid

        self.loss_func = lambda x, y: (x - y).pow(2).sum().mean()

    def train(self, data_x, data_y, EPOCHS=500):

        # x = torch.from_numpy(data_x[:train_size, :])
        # y = torch.from_numpy(data_y[:train_size, :])
        x = torch.from_numpy(data_x)
        y = torch.from_numpy(data_y)

        for t in range(EPOCHS):
            pre = 0
            for bt in range(int(x.shape[0] / self.BATCH)):
                # Forward pass: compute predicted y using operations on Tensors; these
                # are exactly the same operations we used to compute the forward pass using
                # Tensors, but we do not need to keep references to intermediate values since
                # we are not implementing the backward pass by hand.
                y_pred = self.activation_fuc(self.activation_fuc(x[pre:bt * self.BATCH, :] \
                                                                 .mm(self.w1).clamp(min=0), dim=1).mm(self.w2), dim=1)

                # Compute and print loss using operations on Tensors.
                # Now loss is a Tensor of shape (1,)
                # loss.item() gets the scalar value held in the loss.
                loss = self.loss_func(y_pred, y[pre:bt * self.BATCH, :])

                # Use autograd to compute the backward pass. This call will compute the
                # gradient of loss with respect to all Tensors with requires_grad=True.
                # After this call w1.grad and w2.grad will be Tensors holding the gradient
                # of the loss with respect to w1 and w2 respectively.
                loss.backward()

                # Manually update weights using gradient descent. Wrap in torch.no_grad()
                # because weights have requires_grad=True, but we don't need to track this
                # in autograd.
                # An alternative way is to operate on weight.data and weight.grad.data.
                # Recall that tensor.data gives a tensor that shares the storage with
                # tensor, but doesn't track history.
                # You can also use torch.optim.SGD to achieve this.
                with torch.no_grad():
                    self.w1 -= self.lr * self.w1.grad
                    self.w2 -= self.lr * self.w2.grad

                    # Manually zero the gradients after updating weights
                    self.w1.grad.zero_()
                    self.w2.grad.zero_()

                pre = bt * self.BATCH
            if t % 100 == 99:
                print(t, loss.item())

        pass

    def query_class(self, data_x):

        y_pred = self.query_prob(data_x)

        return y_pred.argmax(dim=1)

    def query_prob(self, data_x):
        x = torch.from_numpy(data_x)
        y = torch.from_numpy(data_y)

        y_pred = x.mm(self.w1).clamp(min=0).mm(self.w2)

        return y_pred

    def cal_score(self, targets, pred):

        print('targets:\n{0}'.format(targets))
        print('pred:\n{0}'.format(pred))

        return cal_accuration(targets, pred)

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

    test_nn()


    INPUT_NODES = 28*28
    HIDDEN_NODES = 100
    OUTPUT_NODES = 10
    learning_rate = 0.5

    #cmp sklearn
    # prepare data
    mnist_x, mnist_y = get_mnist_data()

    train_size = 900
    test_size = 100

    data_x, data_y = data_to_arr()

    cmp_skl_knn(data_x[:train_size, :], mnist_y[:train_size], data_x[-test_size - 1:, :], mnist_y[-test_size - 1:])

    #cmp torch
    t_nn = torchNN(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, 0.01)

    t_nn.train(data_x[:train_size, :], data_y[:train_size])

    print(t_nn.cal_score(data_y[train_size:], t_nn.query_class(data_x[train_size:, :])))


