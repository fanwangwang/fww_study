import matplotlib.pyplot as plt

import numpy as np
from scipy.sparse import csc_matrix, csr_matrix, spdiags, triu, tril, find, hstack, eye
from scipy.sparse.linalg import cg, inv, dsolve
from scipy.linalg import norm

from mesh import squaremesh, showmesh, TriangleMesh
from quatrature import TriangleQuadrature


"""

"""

def f(p):
    """ The right hand side of Possion equation
    INPUT:
        p: array object, N*2 
    """
    x = p[:, [0]]
    y = p[:, [1]]
    pi = np.pi
    rhs = 2*pi*pi*np.cos(pi*x)*np.cos(pi*y)
    return rhs

def u(p):
    """ The exact solution 
    """
    x = p[:, [0]]
    y = p[:, [1]]
    pi = np.pi
    u = np.cos(pi*x)*np.cos(pi*y)
    return u

def gd(p):
    """ Dilichlet boundary condition
    """
    return u(p)

def du(p):
    """ The gradient of the exact solution 
    """
    x = p[:, [0]]
    y = p[:, [1]]
    pi = np.pi
    uprime = np.zeros(p.shape, dtype=np.float)
    uprime[:, [0]] = -pi*np.sin(pi*x)*np.cos(pi*y)
    uprime[:, [1]] = -pi*np.cos(pi*x)*np.sin(pi*y)
    return uprime


# Mesh 
mesh = squaremesh(0, 1, 0, 1, 4)

N = mesh.points.shape[0]
NC = mesh.cells.shape[0]
# construct the matrix  
Dlambda, area = mesh.grad_lambda()

idx0 = mesh.cells[:, 0]
idx1 = mesh.cells[:, 1]
idx2 = mesh.cells[:, 2]

I = np.concatenate((
    idx0, idx0, idx0,
    idx1, idx1, idx1,
    idx2, idx2, idx2))
J = np.concatenate((
    idx0, idx1, idx2,
    idx0, idx1, idx2,
    idx0, idx1, idx2))

A00 = np.sum(Dlambda[0]*Dlambda[0], axis=1)*area.flatten()
A01 = np.sum(Dlambda[0]*Dlambda[1], axis=1)*area.flatten()
A02 = np.sum(Dlambda[0]*Dlambda[2], axis=1)*area.flatten()
A11 = np.sum(Dlambda[1]*Dlambda[1], axis=1)*area.flatten()
A12 = np.sum(Dlambda[1]*Dlambda[2], axis=1)*area.flatten()
A22 = np.sum(Dlambda[2]*Dlambda[2], axis=1)*area.flatten()

val = np.concatenate((
    A00, A01, A02,
    A01, A11, A12,
    A02, A12, A22))

A = csc_matrix((val, (I, J)), shape=(N, N))
print(A)
# compute the right hand side vector

qf = TriangleQuadrature(3)
nQuad = qf.get_number_of_quad_points()
b = np.zeros((NC, 3), dtype=np.float)
for i in range(nQuad):
    lam, w = qf.get_gauss_point_and_weight(i)
    p = mesh.to_points(lam)
    fval = f(p)
    for j in range(3):
        b[:, [j]] += fval*lam[j]*w

b *= area
b = np.bincount(mesh.cells.flatten(), weights=b.flatten())
b.shape = (b.shape[0], 1)
print(b)
# Deal with boundary condition
isBdNode = mesh.is_boundary_node()
isFreeNode = isBdNode == False
uh = np.zeros((N, 1), dtype=np.float)

uh[isBdNode] = u(mesh.points[isBdNode, :])

b -= A@uh
uh[isFreeNode] = inv(A[np.ix_(isFreeNode, isFreeNode)])@b[isFreeNode]
eu = u(mesh.points)
error = np.sqrt(np.sum((eu - uh)**2)/N)
print(error)
    




fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
showmesh(mesh, ax)
plt.show()

