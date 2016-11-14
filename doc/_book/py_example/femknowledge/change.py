#给定一个$5×4$ 的矩阵，把它变成 $4×5$ $2*10$ 的列向量，并且每隔 $4$ 行取一个元素  

import numpy as np

A = np.array([[1,2,3,3],[1,2,3,4],[1,1,2,3],[2,0,0,2],[0,0,1,2]])
print(A)
a = np.reshape(A,(4,5))
print(a)
B = np.reshape(A,(4,5),order = 'F')
C = np.reshape(A,(4,5),order = 'C')
print(B)
print(C)

# 变换的时候默认是‘C’，如果加‘order = 'F'’，则是按列排列，例如变换成 $m×n$ 矩阵，
# 则取先取第一列的前 $m$ 个元素组成一行，再接着按列取$m$个元素组成第二行...
