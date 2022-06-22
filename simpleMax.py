import numpy as np
from numpy import linalg as la
from scipy.linalg import eig
np.set_printoptions(linewidth=1000)


matrix = np.array([[-0.168700, 0.353699, 0.008540, 0.733624],
                [0.353699, 0.056519, 0.723182, -0.076440],
                [0.008540, -0.723182, 0.015938, 0.342333],
                [0.733624, -0.076440, 0.342333, -0.045744]], float)

matrix1 = np.array([[2, 1, 1],
                [1, 2.5, 1],
                [1, 1, 3]], float)


eps = 10 ** -8
count = 0

x = np.array([1] * matrix.shape[0])
y = np.dot(matrix, x)
lamda = y * x
new_x = y / la.norm(y)

while(la.norm(new_x*np.sign(lamda) - x) > eps):
    x = new_x
    y = np.dot(matrix, x)
    lamda = np.dot(y,x)
    new_x = y / la.norm(y)
    count += 1

print('Итераций:', count,'Max:', lamda)
w, i = eig(matrix)
print('numpy',w)
#
# matrix = np.array([[2.2, 1, 0.5, 2],
#                 [1, 1.3, 2, 1],
#                 [0.5, 2, 0.5, 1.6],
#                 [2, 1, 1.6, 2]], float)
