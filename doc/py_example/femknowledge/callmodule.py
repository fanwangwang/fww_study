# 导入一个软件的模块，例如导入numpy模块,求圆的面积

import numpy as np
def f(r):
    pi = np.pi
    result = pi*r*r
    return result
    print(result)
print(f(1))
print(f(5))

a = np.array([1.0,2.0])
b = np.array([0.0,0.0])
c = np.array([1.0,3.0])
s = (a-b)*(c-b)*0.5
print(s)
