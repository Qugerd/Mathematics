import numpy as np
import numpy.linalg as lin
from numpy import sqrt
from massive import a, b

np.set_printoptions(linewidth=1000)

n = a.shape[0]
q = a.copy()
GS_b = np.zeros(n)

for i in range(n):
    for j in range(i):
        GS_b += (np.dot(a[:, i], q[:, j]) / np.dot(q[:, j], q[:, j])) * q[:, j]

    q[:, i] = a[:, i] - GS_b
    q[:, i] = q[:, i] / sqrt(np.dot(q[:, i], q[:, i]))
    GS_b = np.zeros(n)

r = lin.inv(q).dot(a)
x = np.round((lin.inv(r).dot(np.transpose(q))).dot(b), 7)
print(x)