from numpy import array, zeros, fabs, set_printoptions
set_printoptions(precision=2, suppress=True)

# a = array([[0, 2, 0, 1],
#  	    [2, 2, 3, 2],
#  	    [4, -3, 0, 1],
#  	    [6, 1, -6, -5]], float)

a = array([[0.411, 0.421, -0.333, 0.313, -0.141, -0.381, 0.245],
                   [0.241, 0.705, 0.139, -0.409, 0.321, 0.0625, 0.101],
                   [0.123, -0.239, 0.502, 0.901, 0.243, 0.819, 0.321],
                   [0.413, 0.309, 0.801, 0.865, 0.423, 0.118, 0.183],
                   [0.241, -0.221, -0.243, 0.134, 1.274, 0.712, 0.423],
                   [0.281, 0.525, 0.719, 0.118, -0.974, 0.808, 0.923],
                   [0.246, -0.301, 0.231, 0.813, -0.702, 1.223, 1.105]], float)


b = array([ 0.096,
                    1.252,
                    1.024,
                    1.023,
                    1.155,
                    1.937,
                    1.673], float)

n = len(b)


for k in range(n):
    if fabs(a[k, k]) == 0:
        for i in range(k + 1, n):
            if fabs(a[i, k]) > fabs(a[k, k]):
                for j in range(k, n):
                    a[k, j], a[i, j] = a[i, j], a[k, j]

                b[k], b[i] = b[i], b[k]
                break

    head = a[k, k]
    for j in range(k, n):
        a[k, j] /= head
    b[k] /= head

    for i in range(n):
        if i == k or a[i, k] == 0: continue
        temp = a[i, k]
        for j in range(k, n):
            a[i, j] -= temp * a[k, j]
        b[i] -= temp * b[k]


print(a)
print(b)
