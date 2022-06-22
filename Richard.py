import math
import numpy as np
from numpy import linalg as la

A = np.array([[1, 2, 1, 4],
                    [2, 0, 4, 3],
                    [4, 2, 2, 1],
                    [-3, 1, 3, 2]])

b = np.array([-13,
                   -28,
                   -20,
                   -6])
eps = 10 ** -5

def richardson(matrix, vector, maxSelf, minSelf, n):
    matrix = np.array(matrix)
    x_prev = np.array([0] * matrix.shape[0])
    x = np.array([1] * matrix.shape[0])

    tau = 2 / (minSelf + maxSelf)
    mu = minSelf / maxSelf
    p = (1 - mu) / (1 + mu)
    iteration = 0
    count = 0
    while (la.norm(x_prev - x) >= eps):
        for k in range(1, n + 1):
            x_prev = x
            nu = math.cos((2 * k - 1) * math.pi / (2 * n))
            tau_k = tau / (1 - p * nu)
            x = (vector - matrix @ x_prev) * tau_k + x_prev
            iteration += 1
            print(iteration, 'iter', x)
        count += 1
    print(count)
    return x


n = 10
ls = la.eig(A)[0]
minSelf, maxSelf = min(ls), max(ls)
richardson(A, b, maxSelf, minSelf, n)

a = np.array([[1, 3, -2, 0, -2, 0.5],
                [3, 4, -5, 1, -3, 5.4],
                [-2, -5, 3, -2, 2, 5.0],
                [0, 1, -2, 5, 3, 7.5],
                [-2, -3, 2, 3, 4, 3.3]], float)

b = np.array([0.5,
              5.4,
              5.0,
              7.5,
              3.3])


a = np.array([[1, 3, -2, 0, -2],
                [3, 4, -5, 1, -3],
                [-2, -5, 3, -2, 2],
                [0, 1, -2, 5, 3],
                [-2, -3, 2, 3, 4]], float)