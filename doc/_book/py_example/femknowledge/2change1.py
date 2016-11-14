#如何把一个numpy的二维数组array展开成一个一维数组array
#例如，把一个二维数组a = [[1,2,3,4,5],[2,3,4,5,6]]展开成一维数组

import numpy as np

a = [[1,2,3,4,5],[2,3,4,5,6]]
a = np.array(a)
print(a)
b = a.flatten()
print(b)
