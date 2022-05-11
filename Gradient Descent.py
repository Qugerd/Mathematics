import numpy as np
from massive import a, b

def gradient(data, data_2):
    n = data.shape[0]
    eps = 10 ** -10
    x = np.zeros(n)
    a = data
    b = data_2

    k = 0
    while True:
        k += 1
        print(k)
        f = a.dot(x) - b
        if max(abs(f)) < eps:
            return x

        r = -f
        lambd = (r.dot(r)) / (r.dot(a.dot(r)))
        x = x - f.dot(lambd)

print(gradient(a, b))