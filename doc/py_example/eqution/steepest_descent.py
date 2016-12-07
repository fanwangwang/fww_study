import numpy as np

def f(x):
    f = 2*x[0]**2+x[1]**2
    return f
def df(x):
    return np.array([4*x[0],2*x[1]])

def norm(x):
    return np.sqrt(x[0]**2+x[1]**2)
def phi(x):
    h = np.zeros(5)
    for i in range(5):
        p = x[i] + h[i]*d[i]
        phi = f(p)
    return phi

#参数初始化
n=5
x = np.zeros((n,2))
x[0] = np.array([1,1])
epsilon = 0.1

d  = np.zeros((n,2))
d[0] = -df(x[0])
print(d[0])
    
if norm(d[0])>0.1:
    for i in range(5):
        g = phi(x[i])
        print(g)
        x[i+1] = x[i] + h[i]*d[i]
        print(x[i])
else:
    print('end')
