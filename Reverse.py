import numpy as np
from numpy import linalg as la
from scipy.linalg import eig
from inverse import inverse
np.set_printoptions(linewidth=1000)



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
        x = np.round(inverse(matrix, v), 10)

        new_alpha = np.amax((x))
        lam = 1 / alpha
        iteration += 1

    print('Итераций:', iteration, 'Лабда:', lam)
    return lam


matrix = np.array([[-0.168700, 0.353699, 0.008540, 0.733624],
                [0.353699, 0.056519, 0.723182, -0.076440],
                [0.008540, -0.723182, 0.015938, 0.342333],
                [0.733624, -0.076440, 0.342333, -0.045744]], float)

matrix1 = np.array([[2, 1, 1],
                [1, 2.5, 1],
                [1, 1, 3]], float)

eps = 10 ** -8

reverseIteration(matrix1, eps)

w, i = eig(matrix)
print('numpy',w)