from contextlib import AbstractAsyncContextManager
import numpy as np
from numpy import linalg as la

from inverse import inverse, createInverse


def reverseIteration(matrix, eps):
    x = np.array([1] * matrix.shape[0])
    x0 = np.array([2] * matrix.shape[0])
    alpha = np.max(x)
    new_alpha = np.max(x0)
    lam = 1 / alpha
    iteration = 0

    while (la.norm(1 / alpha - 1 / new_alpha)) >= eps:
        alpha = new_alpha
        v = x / alpha
        x = np.round(inverse(matrix, v), 3)

        new_alpha = np.amax((x))
        lam = 1 / alpha
        iteration += 1
        print('iter', iteration, lam)

    return lam

eps = 10 ** -8
matrix = np.array([[2.2, 1, 0.5, 2],
                [1, 1.3, 2, 1],
                [0.5, 2, 0.5, 1.6],
                [2, 1, 1.6, 2]], float)



reverseIteration(matrix, eps)
w, i = la.eig(matrix)
print('numpy',w)


a_data = ([1, 2, 3],
          [2, 2, 3],
          [3, 3, 3],
          [4, 7, 0])

b_data = ([4, 7, 0, 4])