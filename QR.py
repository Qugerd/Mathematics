import math
import numpy as np
from numpy.linalg import solve

np.set_printoptions(linewidth=1000)
np.set_printoptions(precision=4, floatmode='fixed')


def Tau(a):
    if a >= 0:
        return 1
    else:
        return -1

matrix = matrix1 = [[2.2, 4, -3, 1.5, 0.6, 2, 0.7],
        [4, 3.2, 1.5, -0.7, -0.8, 3, 1],
        [-3, 1.5, 1.8, 0.9, 3, 2, 2],
        [1.5, -0.7, 0.9, 2.2, 4, 3, 1],
        [0.6, -0.8, 3, 4, 3.2, 0.6, 0.7],
        [2, 3, 2, 3, 0.6, 2.2, 4],
        [0.7, 1, 2, 1, 0.7, 4, 3.2]]

b = b1 = [3.2, 4.3, 0.1, 3.5, 5.3, 9, 3.7]


n = int(len(matrix))
matrix = np.array(matrix)

for k in range(n):
    p = np.zeros(n)
    sum = 0

    for l in range(k, n):
        sum += matrix[l][k] ** 2
    p[k] = matrix[k][k] + Tau(matrix[k][k]) * (sum ** (1/2))

    for l in range(k + 1, n):
        p[l] = matrix[l][k]

    new_matrix = np.zeros(shape=(n,n))
    new_matrix[:k][:] = matrix[:k][:]
    f = np.zeros(n)

    for i in range(k,n):
        sum = 0
        for l in range(k, n):
             sum += matrix[l][k] ** 2

        new_matrix[k][k] = -Tau(matrix[k][k]) * (sum ** (1 / 2))
        for j in range(k + 1, n):
            sum1 = 0
            for l in range(k, n):
                sum1 += p[l] * matrix[l][j]

            sum2 = 0
            for l in range(k, n):
                sum2 += p[l] ** 2
            new_matrix[i][j] = matrix[i][j] - 2 * p[i] * (sum1) / (sum2)

    for i in range(n):
        sum1 = 0
        for l in range(k, n):
            sum1 += p[l] * b[l]

        sum2 = 0
        for l in range(k, n):
            sum2 += p[l] ** 2
        f[i] = b[i] - 2 * p[i] * (sum1) / (sum2)

    matrix = new_matrix
    b = f


x = np.zeros(n)
for i in range(n - 1, -1, -1):
    sum = 0
    for j in range(n):
        sum += x[j] * matrix[i][j]
    x[i] = (b[i] - sum) / matrix[i][i]

print("Результат:", x)

temp = solve(matrix1, b1)
print("Точное решение:", temp)

print("Разница:")
diff = []
for i in range(n):
    diff.append(math.fabs(temp[i] - x[i].real))
print(diff)