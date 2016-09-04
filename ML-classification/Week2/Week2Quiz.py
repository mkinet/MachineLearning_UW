import numpy as np


def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))
    return sig


x = [2.5, 0.3, 2.8, 0.5]
y = [1, -1, 1, 1]

# Q4
lik = sigmoid(x[0]) * (1 - sigmoid(x[1])) * sigmoid(x[2]) * sigmoid(x[3])
print(lik)

# Q5

x[0] * (1 - sigmoid(x[0])) - x[1] * sigmoid(x[1]) + x[2] * \
    (1 - sigmoid(x[2])) + x[3] * (1 - sigmoid(x[3]))
