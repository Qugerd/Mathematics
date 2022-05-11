import numpy as np
from massive import a, b

f = b
A = a
n = len(f)
xp = x = np.array([0.0] * n)
x_1 = f
o = 0


w = 1.0
eps = 10 ** -10

while max(abs(xp - x_1) > eps):
    x_1 = x.copy()
    x = np.zeros(n)
    o += 1
    for i in range(n):
        S1 = sum((A[i, j] * x[j] for j in range(i)))
        S2 = sum((A[i, j] * xp[j] for j in range(i + 1, n)))
        x[i] = (w * (f[i] - S1 - S2) + (1 - w) * A[i, i] * xp[i]) / A[i, i]

    xp = x

print(x)
print("Число итераций:", o)