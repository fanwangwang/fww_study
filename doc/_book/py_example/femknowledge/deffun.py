# 定义一个函数 $f = \cos \pi x\cos\pi y$,输入参数 $N×2$
# 的矩阵，每一行代表一个二维点 $[x,y]$，返回这些点处所对应的值以及梯度函数的值

import numpy as np
pi = np.pi
p = np.array([[1,2],[2,1],[0,0],[1,1],[2,2]])
def f(p):
    x = p[:,[0]]
    y = p[:,[1]]
    f = np.cos(pi*x)*np.cos(pi*y)
    return f
def df(p):
    x = p[:,[0]]
    y = p[:,[1]]
    fprime = np.zeros(p.shape,dtype = np.int)
    fprime[:,[0]] = -pi*np.sin(pi*x)*np.cos(pi*y)
    fprime[:,[1]] = -pi*np.cos(pi*x)*np.sin(pi*y)
    return fprime
print(f(p))
print(df(p))
