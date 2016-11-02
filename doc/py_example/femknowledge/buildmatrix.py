#如何建立一个矩阵 $A = (i+j+1)_(i,j)$

import numpy as np
n = 3
A1 = np.zeros((n,n))
A2 = np.zeros((n,n))
A3 = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        A1[i][j] = i
        A2[i][j] = j
        A3[i][j] = 1
        A = A1 + A2 + A3
        print(A)
