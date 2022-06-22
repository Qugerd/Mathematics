import math
import numpy as np
from numpy import linalg as la

EPS = 10 ** -2
n=5

a = np.array([[16, 2, 0, -2],
                [4, 20, 1, 0],
                [2, 0, 10, 0],
                [-4, 0, 4, 32]], float)


b = np.array([13, 24, 7, 0], float)

def richardson(matrix, vector, maxSelf, minSelf, n):
    x_prev = np.array([0] * matrix.shape[0])
    x = np.array([1] * matrix.shape[0])
    tau = 2 / (minSelf + maxSelf)
    mu = minSelf / maxSelf
    p = (1 - mu) / (1 + mu)
    iteration = 0

    while (la.norm(x_prev - x) >= EPS):
        for k in range(1, n + 1):
            x_prev = x
            nu = math.cos((2 * k - 1) * math.pi / (2 * n))
            tau_k = tau / (1 - p * nu)
            x = (vector - matrix @ x_prev) * tau_k + x_prev
            iteration += 1
            print(iteration, 'Итераций:', x)

    return x

ls = la.eig(a)[0]
min, max = ls.min(), ls.max()
richardson(a, b, max, min, n)