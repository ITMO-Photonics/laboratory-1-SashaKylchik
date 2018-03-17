
import scipy.linalg as lng
import numpy as np
N = 5
A = np.zeros((N,N))

i,j = np.indices((N,N))
A[i == j] = 1
A[i == j+1] = 1
A[i == j+2] = 1
b = np.arange(N)


B = np.linalg.solve(A, b)
print(B);
