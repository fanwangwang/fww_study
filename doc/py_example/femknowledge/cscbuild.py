#给定一个小规模的稀疏矩阵，建立一个CSR或者CSC格式的稀疏矩阵
#例如，给定一个 $5×5$ 的稀疏矩阵，建立一个CSR和CSC格式的稀疏矩阵
import numpy as np
from scipy.sparse import csc_matrix,csr_matrix
A = [[2,1,0,0,0],[0,0,1,2,0],[0,2,0,0,1],[1,0,0,0,2],[1,0,2,0,0]]
#print(A)
for i in range(5):
    for j in range(5):
        if A[i][j] != 0:
            print(A[i][j],i,j)


val = [2,1,1,2,2,1,1,2,1,2]
i = [0,0,1,1,2,2,3,3,4,4]
j = [0,1,2,3,1,4,0,4,0,2]
A = csc_matrix((val,(i,j)),shape = (5,5))
print(A)
B = csr_matrix((val,(i,j)),shape = (5,5))
print(B)
