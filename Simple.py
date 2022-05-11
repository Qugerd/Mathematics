import numpy as np
from massive import A

# [0.68505222 1.03484008 0.56298956 0.01525783]

n = A.shape[0]
eps = 10 ** -10

x = np.zeros(n)
x_0 = np.squeeze(np.asarray(A[:, len(A[0]) - 1:]))
c = A.copy()
k = 0

for i in range(n):
    for j in range(n + 1):
        c[i, j] = -A[i, j] / A[i, i]
        if j == n:
             c[i, j] *= -1

while max(abs(x - x_0) > eps):
    k += 1
    x_0 = x.copy()
    x = np.zeros(n)
    for i in range(n):
        for j in range(n + 1):
            if j != n:
                x[i] += c[i, j] * x_0[j]
            else:
                x[i] += c[i, j]

        x[i] -= c[i, i] * x_0[i]

print(x)
print('Число итераций:', k)