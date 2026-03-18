import numpy as np

X = np.array([
    [50, 1],
    [80, 2],
    [120, 3],
    [150, 4]
])

y = np.array([160, 230, 310, 380])

w = np.array([0.0, 0.0])
b = 0.0

learning_rate = 0.0001
iterations = 10000
m = len(X)

for i in range(iterations):

    predictions = np.dot(X, w) + b
    errors = predictions - y

    dw = (1/m) * np.dot(X.T, errors)
    db = (1/m) * np.sum(errors)

    w = w - learning_rate * dw
    b = b - learning_rate * db

print("weights:", w)
print("bias:", b)
