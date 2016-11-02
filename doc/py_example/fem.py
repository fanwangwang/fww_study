import matplotlib.pyplot as plt

import numpy as np
from scipy.sparse import csc_matrix, csr_matrix, spdiags, triu, tril, find, hstack, eye
from scipy.sparse.linalg import cg, inv, dsolve
from scipy.linalg import norm

from mesh import squaremesh, showmesh, TriangleMesh
from quatrature import TriangleQuadrature


"""

"""

def f(p):           #定义一个函数在（x，y）处的值
    """ The right hand side of Possion equation
    INPUT:
        p: array object, N*2 
    """
    x = p[:, [0]]
    y = p[:, [1]]
    pi = np.pi
    rhs = 2*pi*pi*np.cos(pi*x)*np.cos(pi*y)
    return rhs

def u(p):           #真解
    """ The exact solution 
    """
    x = p[:, [0]]
    y = p[:, [1]]
    pi = np.pi
    u = np.cos(pi*x)*np.cos(pi*y)
    return u

def gd(p):          #边界条件
    """ Dilichlet boundary condition
    """
    return u(p)

def du(p):          #函数u的梯度函数
    """ The gradient of the exact solution 
    """
    x = p[:, [0]]
    y = p[:, [1]]
    pi = np.pi
    uprime = np.zeros(p.shape, dtype=np.float)      #对uprime初始化
    uprime[:, [0]] = -pi*np.sin(pi*x)*np.cos(pi*y)  #关于x求导
    uprime[:, [1]] = -pi*np.cos(pi*x)*np.sin(pi*y)  #关于y求导
    return uprime


# Mesh 
mesh = squaremesh(0, 1, 0, 1, 4)

N = mesh.number_of_points()
NT = mesh.number_of_cells()

# construct the matrix  
Dlambda, area = mesh.grad_lambda()

idx0 = mesh.cells[:, 0]                 #每个单元的第0号节点
idx1 = mesh.cells[:, 1]
idx2 = mesh.cells[:, 2]

I = np.concatenate((                    #i，j的指标
    idx0, idx0, idx0,
    idx1, idx1, idx1,
    idx2, idx2, idx2))
J = np.concatenate((
    idx0, idx1, idx2,
    idx0, idx1, idx2,
    idx0, idx1, idx2))
# 计算刚度矩阵的每个元素的值
A00 = np.sum(Dlambda[0]*Dlambda[0], axis=1)*area.flatten()  
A01 = np.sum(Dlambda[0]*Dlambda[1], axis=1)*area.flatten()
A02 = np.sum(Dlambda[0]*Dlambda[2], axis=1)*area.flatten()
A11 = np.sum(Dlambda[1]*Dlambda[1], axis=1)*area.flatten()
A12 = np.sum(Dlambda[1]*Dlambda[2], axis=1)*area.flatten()
A22 = np.sum(Dlambda[2]*Dlambda[2], axis=1)*area.flatten()
# 对应的值
val = np.concatenate((
    A00, A01, A02,
    A01, A11, A12,
    A02, A12, A22))

A = csc_matrix((val, (I, J)), shape=(N, N)) #N×N的稀疏矩阵

# compute the right hand side vector

qf = TriangleQuadrature(3)
nQuad = qf.get_number_of_quad_points()
b = np.zeros((NT, 3), dtype=np.float)
for i in range(nQuad):
    lam, w = qf.get_gauss_point_and_weight(i)
    p = mesh.to_points(lam)
    fval = f(p)
    for j in range(3):
        b[:, [j]] += fval*lam[j]*w

b *= area
b = np.bincount(mesh.cells.flatten(), weights=b.flatten())
b.shape = (b.shape[0], 1)

# Deal with boundary condition
isBdNode = mesh.is_boundary_node()      #网格边界节点
isFreeNode = isBdNode == False          #内部节点
uh = np.zeros((N, 1), dtype=np.float)   

uh[isBdNode] = u(mesh.points[isBdNode, :])

b -= A@uh                               #矩阵与向量的乘积
uh[isFreeNode] = inv(A[np.ix_(isFreeNode, isFreeNode)])@b[isFreeNode]
                                        #求数值解
eu = u(mesh.points)                     #真解

error = np.sqrt(np.sum((eu - uh)**2)/N) #误差
print(error)
    




fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
showmesh(mesh, ax)
plt.show()

