import numpy as np


def dot(a, b):
    if (type(a[0]) != list):
        if (len(a) == len(b)):
            a = [a]
        elif (len(b) == 1):
            a = np.transpose([a])

    if (type(b[0]) != list):
        if (len(a[0]) == len(b)):
            b = np.transpose([b])
        elif (len(a[0]) == 1):
            b = [b]

    if (len(a[0]) == len(b)):
        temp = [[0 for j in range(len(b[0]))] for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                temp[i][j] = sum([a[i][k] * b[k][j] for k in range(len(b))])
        return temp


def mainMinor(matrix, size):
    return [[matrix[i][j] for j in range(size)] for i in range(size)]


def createInverse(matrix):
    size = 1
    prev_inv = [[1 / matrix[0][0]]]

    while (len(prev_inv) < len(matrix)):
        size += 1
        temp_minor = mainMinor(matrix, size)

        v = [temp_minor[size - 1][:-1]]
        u = [[temp_minor[i][size - 1]] for i in range(size - 1)]

        alpha = 1 / (temp_minor[size - 1][size - 1] - dot(dot(v, prev_inv), u)[0][0])

        rn = (np.array(dot(prev_inv, u)) * (-alpha)).tolist()
        qn = (np.array(dot(v, prev_inv)) * (-alpha)).tolist()

        Bn = prev_inv - np.array(dot(dot(prev_inv, u), qn))
        prev_inv = Bn.tolist()

        for i in range(len(rn)):
            prev_inv[i].append(rn[i][0])
        qn[0].append(alpha)
        prev_inv.append(qn[0])
    return prev_inv


def inverse(matrix, vector):
    prev_inv = createInverse(matrix)

    temp = dot(matrix, prev_inv)
    x = dot(prev_inv, vector)

    return (np.transpose(x)[0])

a = np.array([[16, 2, 0, -2],
                [4, 20, 1, 0],
                [2, 0, 10, 0],
                [-4, 0, 4, 32]], float)


b = np.array([13, 24, 7, 0], float)

print(inverse(a, b))
