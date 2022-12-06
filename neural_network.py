import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid activation function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    # Initialize the neural network
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(self.y.shape)

    # Define the feedforward method
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    # Define the backpropagation method
    def backprop(self):
        # Calculate the error
        error = self.y - self.output
        # Calculate the gradient of the error with respect to the output
        d_output = error * sigmoid_derivative(self.output)
        # Calculate the error with respect to the first hidden layer
        error_hidden_layer = d_output.dot(self.weights2.T)
        # Calculate the gradient of the error with respect to the first hidden layer
        d_layer1 = error_hidden_layer * sigmoid_derivative(self.layer1)
        # Update the weights
        self.weights2 += self.layer1.T.dot(d_output)
        self.weights1 += self.input.T.dot(d_layer1)

# Define the input and output data
x = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create a neural network
nn = NeuralNetwork(x, y)

# Train the neural network
for i in range(1500):
    nn.feedforward()
    nn.backprop()

# Print the final output of the neural network
print(nn.output)
