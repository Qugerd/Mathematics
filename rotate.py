from numpy import *
from numpy.linalg import eigh


def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1


def rotate(Matrix, p):
    A = array(copy(Matrix), float)
    n = A.shape[0]

    sigma = 1
    iteration = 1
    while True:
        C = array(zeros([n, n]))

        i = 0
        j = 1
        for g in range(n):
            for h in range(n):
                if g != h:
                    if abs(A[g, h]) > abs(A[i, j]):
                        i = g
                        j = h

        while abs(A[i, j]) < 10 ** -sigma:
            sigma += 1
        if sigma > p or A[i, j] == 0:
            break

        d = sqrt((A[i, i] - A[j, j]) ** 2 + 4 * A[i, j] ** 2)
        s = sgn(A[i, j] * (A[i, i] - A[j, j])) * sqrt((1 - abs(A[i, i] - A[j, j]) / d) / 2)
        c = sqrt((1 + abs(A[i, i] - A[j, j]) / d) / 2)

        for k in [w for w in range(0, min(i, j))] + [w for w in range(min(i, j) + 1, max(i, j))] + [w for w in
                                                                                                    range(max(i, j) + 1,
                                                                                                          n)]:
            for l in [w for w in range(0, min(i, j))] + [w for w in range(min(i, j) + 1, max(i, j))] + [w for w in
                                                                                                        range(max(i,
                                                                                                                  j) + 1,
                                                                                                              n)]:
                C[k, l] = A[k, l]

        for k in range(n):
            if k != i and k != j:
                C[k, i] = c * A[k, i] + s * A[k, j]
                C[i, k] = C[k, i]
                C[k, j] = -s * A[k, i] + c * A[k, j]
                C[j, k] = C[k, j]

        C[i, i] = c ** 2 * A[i, i] + 2 * c * s * A[i, j] + s ** 2 * A[j, j]
        C[j, j] = s ** 2 * A[i, i] - 2 * c * s * A[i, j] + c ** 2 * A[j, j]

        iteration += 1

        A = C

    lambd = [A[i, i] for i in range(n)]
    return lambd


# data=([[1.0, 0.42, 0.54, 0.66],
#    [0.42, 1.0, 0.32, 0.44],
#   [0.54, 0.32, 1.0, 0.22],
#  [0.66, 0.44, 0.22, 1.0]])


data = [[20, -10, -2, 26],
        [-10, 18, -3, 7],
        [-2, -3, 111, -9],
        [26, 7, -9, 160]]

if __name__ == "__main__":
    set_printoptions(linewidth=1000)
    set_printoptions(precision=4, floatmode='fixed')

    p = 4
    A = array(data, float)
    lambd = rotate(A, 4)

    print('solution:', lambd)

    pysolv = eigh(A)[0]
    print('python solution:', pysolv)

    lambd.sort()
    pysolv.sort()

    print('Разница:', pysolv - lambd)
    print('Epsilon = 0.0001', )
