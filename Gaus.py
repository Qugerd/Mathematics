from numpy import array, zeros, fabs

a = array([[0, 7, -1, 3, 1],
    [0, 3, 4, 1, 7],
    [6, 2, 0, 2, -1],
    [2, 1, 2, 0, 2],
    [3, 4, 1, -2, 1]])


b = array([5, 7, 2, 3, 4])

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
x = zeros(n, float)

for k in range(n - 1):
    if fabs(a[k, k]) == 0:
        for i in range(k + 1, n):
            if fabs(a[i, k]) > fabs(a[k, k]):
                a[[k, i]] = a[[i, k]]
                b[[k, i]] = b[[i, k]]
                break

    for i in range(k + 1, n):
        if a[i, k] == 0: continue
        temp = a[k, k] / a[i, k]
        for j in range(k, n):
            a[i, j] = a[k, j] - a[i, j] * temp

        b[i] = b[k] - b[i] * temp

print(a)
print(b)

x[n - 1] = b[n - 1] / a[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    sum = 0
    for j in range(i + 1, n):
        sum += a[i, j] * x[j]
    x[i] = (b[i] - sum) / a[i, i]

print(x)