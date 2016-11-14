#给定一个矩阵，显示该矩阵的行数和列数
#给定一个矩阵A= [[1,2,3,4],[1,3,4,5],[2,3,4,5]],显示他的行数和列数

import numpy as np
A = np.array([[1,2,3,4],[1,3,4,5],[2,3,4,5]])
a = A.shape[0]
b = A.shape[1]
print(a)
print(b)
B = A.flatten()
print(B)



