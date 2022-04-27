import colorama
import numpy as np

np.set_printoptions(linewidth=1000)

H = [
    [2.2, 4, -3, 1.5, 0.6, 2, 0.7],
    [4, 3.2, 1.5, -0.7, -0.8, 3, 1],
    [-3, 1.5, 1.8, 0.9, 3, 2, 2],
    [1.5, -0.7, 0.9, 2.2, 4, 3, 1],
    [0.6, -0.8, 3, 4, 3.2, 0.6, 0.7],
    [2, 3, 2, 3, 0.6, 2.2, 4],
    [0.7, 1, 2, 1, 0.7, 4, 3.2]
]

a = np.array(H, complex)

L = np.zeros_like(a)
n,_ = np.shape(a)

for j in range(n):
    for i in range(j, n):
        if i == j:
            L[i, j] = np.sqrt(a[i, j] - np.sum(L[i, :j] ** 2))
        else:
            L[i, j] = (a[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]


print(np.transpose(L))

print(np.around(np.dot(L, np.transpose(L)), decimals=1))


