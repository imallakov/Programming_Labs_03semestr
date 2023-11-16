import numpy as np

A = np.array([[1, 2, -14, 0, -8],
                [3, 2, 13, 0, 8],
                [0, -1, 7, 1, 0],
                [2, -3, 10, 4, 8],
                [1, -3, 8, -2, 13]])
AT = A.T
print(AT)

Ainv = np.linalg.inv(A)
print(np.linalg.inv(Ainv))

B = np.random.randint(low=-30, high=25, size=(4,6))
print(B)

I = np.argwhere(B>5)
print(I)

J = np.argwhere((B >7) | (B <0))
print(J)
