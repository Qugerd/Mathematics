import math
import numpy as np
from numpy import linalg as la

A = np.matrix([
    [10.9, 1.2, 2.1, 0.9],
    [1.2, 11.2, 1.5, 2.5],
    [2.1, 1.5, 9.8, 1.3],
    [0.9, 2.5, 1.3, 12.1]
])

b = np.array([-7.0, 5.3, 10.3, 24.6])
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
