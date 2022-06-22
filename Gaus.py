from numpy import array, zeros, fabs

a = array([[0, 7, -1, 3, 1],
    [0, 3, 4, 1, 7],
    [6, 2, 0, 2, -1],
    [2, 1, 2, 0, 2],
    [3, 4, 1, -2, 1]])


b = array([5, 7, 2, 3, 4])

a = array([[1, 3, -2, 0, -2],
                [3, 4, -5, 1, -3],
                [-2, -5, 3, -2, 2],
                [0, 1, -2, 5, 3],
                [-2, -3, 2, 3, 4]], float)

b = array([0.5,
              5.4,
              5.0,
              7.5,
              3.3], float)

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