import numpy as np
from math import sqrt
from scipy.linalg import eig
#
# m = [
# 	[2 , 1  , 1],
# 	[1 , 2.5, 1],
# 	[1 , 1  , 3],
# ]
# np.set_printoptions(precision=2, suppress=True)


m= [[16, 2, 0, -2],
                [4, 20, 1, 0],
                [2, 0, 10, 0],
                [-4, 0, 4, 32]]

def sgn(num):
    return 1 if num > 0 else -1


def get_max_index(a):
    mi, mj = 0, 1
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (i != j and abs(a[i][j]) > abs(a[mi][mj])):
                mi, mj = i, j
    return [mi, mj]


def solve(a, p):
    o=[]
    for i in range(p):
        o.append(10 ** (-(i + 1)))

    a = [r[:] for r in a]
    count = 0

    for p in o:
        i, j = get_max_index(a)

        while (abs(a[i][j]) >= p):
            d = sqrt(((a[i][i] - a[j][j]) ** 2 + 4 * (a[i][j]) ** 2))
            c = sqrt((0.5 * (1 + abs(a[i][i] - a[j][j]) / d)))
            s = sgn(a[i][j] * (a[i][i] - a[j][j])) * sqrt((0.5 * (1 - abs(a[i][i] - a[j][j]) / d)))

            C = [r[:] for r in a]

            C[i][j], C[j][i] = 0, 0

            for k in range(len(a)):
                if (k == i or k == j):
                    continue

                C[i][k] = c * a[k][i] + s * a[k][j]
                C[k][i] = C[i][k]

                C[j][k] = -s * a[k][i] + c * a[k][j]
                C[k][j] = C[j][k]

            C[i][i] = c * c * a[i][i] + 2 * c * s * a[i][j] + s * s * a[j][j]
            C[j][j] = s * s * a[i][i] - 2 * c * s * a[i][j] + c * c * a[j][j]

            a = C
            i, j = get_max_index(a)
            count += 1

    print(count)
    return [a[i][i] for i in range(len(a))]


m = solve(m, 1)
e = np.eye(len(m))
for i in range(len(m)):
	e[i][i] *= m[i]

e *= -1
a = m + e


print(m)

m1 = np.array([[16, 2, 0, -2],
                [4, 20, 1, 0],
                [2, 0, 10, 0],
                [-4, 0, 4, 32]], float)


m2 = np.array([13, 24, 7, 0], float)


