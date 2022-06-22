from cmath import sqrt
import numpy as np
np.set_printoptions(linewidth=1000)

def createS(matrix):
    size = matrix.shape[0]
    matrixS = np.zeros((size, size), dtype=complex)
    matrixS[0] = matrix[0] / sqrt(matrix[0][0])
    matrixS[0][0] = sqrt(matrix[0][0])

    for i in range(size):
        matrixS[i][i] = sqrt(matrix[i][i] - sum((matrixS[k][i]) ** 2 for k in range(i)))
        for j in range(i, size):
            matrixS[i][j] = (matrix[i][j] - sum((matrixS[k][i] * matrixS[k][j]) for k in range(i))) / matrixS[i][i]

    return matrixS


def getAnsver(s, v):
    size = s.shape[0]
    y = np.zeros(size, dtype=complex)

    for i in range(len(s)):
        y[i] = (v[i] - sum([s[k][i] * y[k] for k in range(i)])) / s[i][i]

    return y


def solveTriangular(matrix, y):
    n = matrix.shape[0]
    x = np.zeros(n, dtype=complex)

    for i in range(n):
        for j in range(i):
            y[n - 1 - i] -= matrix[n - 1 - i][n - 1 - j] * x[n - 1 - j]
        x[n - 1 - i] = y[n - 1 - i] / matrix[n - 1 - i][n - 1 - i]

    return x


def squareRoot(matrix, vector):
    matrix = matrix.copy()
    vector = vector.copy()

    matrixS = createS(matrix)
    y = getAnsver(matrixS, vector)
    x = solveTriangular(matrixS, y)

    return x

a = np.array([[1, 3, -2, 0, -2],
                [3, 4, -5, 1, -3],
                [-2, -5, 3, -2, 2],
                [0, 1, -2, 5, 3],
                [-2, -3, 2, 3, 4]], float)

b = np.array([0.5,
              5.4,
              5.0,
              7.5,
              3.3], float)

print(squareRoot(a, b).real)


















