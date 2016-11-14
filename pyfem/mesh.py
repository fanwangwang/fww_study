import numpy as np
from scipy.sparse import csc_matrix, csr_matrix, spdiags, eye
from scipy.sparse import triu, tril, find, hstack

from matplotlib.tri import Triangulation

from tool import unique_row



class Mesh:
    """
    
    """
    def __init__(self, points, cells):
        """ Constructor
        INPUT:
            points: array object, N*dim matrix, the node coordinates 
            cells: array object, NT*n matrix,  NT elems with n nodes 
        """
        self.points = points 
        self.cells = cells 
    
    def number_of_points(self):
        """ The number of points
        """
        return self.points.shape[0]

    def number_of_cells(self):
        """ The number of cells
        """
        return self.cells.shape[0]

    def geom_dimentsion(self):
        """ The geometric dimension of the mesh
        """ 
        return self.points.shape[1]

    def __str__(self):
        print("Ponts: ")
        print(self.points)
        print("Cells: ")
        print(self.cells)

class TriangleMesh(Mesh):
    """
    Example:
        points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float)
        cells = np.array([[1, 2, 0], [3, 0, 2]], dtype=np.int32)
        mesh = TriangleMesh(points, cells)
    """
    def __init__(self, points, cells):
        """ Constructor
        INPUT:
            points: array object, N*dim matrix, the node coordinates 
            cells: array object, NT*3 matrix,  NT triangle mesh
        """
        Mesh.__init__(self, points, cells)        

    def total_edge(self):
        NC = self.cells.shape[0]
        totalEdge = np.zeros((3*NC, 2), dtype=np.int)
        n = [1, 2, 0]
        p = [2, 0, 1]
        for i in range(3):
            j = i+1
            idx = np.arange(i*NC, j*NC)
            totalEdge[idx, :] = self.cells[:, [n[i], p[i]]]
        totalEdge.sort(axis=1)
        return totalEdge

    def auxstructure(self):
        totalEdge = self.total_edge()
        edge, i, j = unique_row(totalEdge)
        NT = self.cells.shape[0]
        cell2edge = np.reshape(j, (NT, 3), order='F')
        return (edge, cell2edge)

    def is_boundary_node(self):
        N = self.points.shape[0]
        NC = self.cells.shape[0]
        totalEdge = self.total_edge()
        I = np.ones((3*NC, ), dtype=np.int)
        A = csr_matrix((I, (totalEdge[:, 0], totalEdge[:, 1])), shape=(N, N))
        NE = A.getnnz()
        edge = np.zeros((NE, 2), dtype=np.int)
        edge[:, 0], edge[:, 1], val = find(A)
        isBdEdge = val == 1

        isBdNode = np.zeros((N, ), dtype=np.bool)
        isBdNode[edge[isBdEdge, 0]] = True
        isBdNode[edge[isBdEdge, 1]] = True

        return isBdNode 

    def uniform_refine(self, n=1):
        for i in range(n):
            N = self.points.shape[0]
            NC = self.cells.shape[0]
            edge, cell2edge = self.auxstructure()
            NE = edge.shape[0]

            edge2newPoints = np.arange(N, N+NE)

            newPoints = (self.points[edge[:, 0], :] + self.points[edge[:, 1],
                :])/2.0;
            self.points = np.concatenate((self.points, newPoints))

            p = np.concatenate((self.cells, edge2newPoints[cell2edge]), axis=1)
            self.cells = np.concatenate((
                p[:, [0, 5, 4]], 
                p[:, [5, 1, 3]],
                p[:, [4, 3, 2]],
                p[:, [3, 4, 5]]))
        return

    def grad_lambda(self):
        NT = self.number_of_cells()
        points = self.points
        cells = self.cells
        v0 = points[cells[:, 2], :] - points[cells[:, 1], :]
        v1 = points[cells[:, 0], :] - points[cells[:, 2], :]
        v2 = points[cells[:, 1], :] - points[cells[:, 0], :]

        area = 0.5*(-v2[:, [0]]*v1[:, [1]] + v2[:, [1]]*v1[:, [0]])
        Dlambda0 = np.concatenate((-v0[:,[1]], v0[:, [0]]), axis=1)/(2*area)
        Dlambda1 = np.concatenate((-v1[:,[1]], v1[:, [0]]), axis=1)/(2*area)
        Dlambda2 = np.concatenate((-v2[:,[1]], v2[:, [0]]), axis=1)/(2*area)
        Dlambda = [Dlambda0, Dlambda1, Dlambda2]
        return (Dlambda, area)

    def to_points(self, bc):
        points = self.points
        cells = self.cells
        p0 = points[cells[:, 0], :] 
        p1 = points[cells[:, 1], :] 
        p2 = points[cells[:, 2], :] 
        return bc[0]*p0+ bc[1]*p1 + bc[2]*p2

def showmesh(mesh, ax):
    tri = Triangulation(mesh.points[:, 0], mesh.points[:, 1], mesh.cells)
    ax.set_aspect('equal')
    ax.triplot(tri)
    ax.set_axis_off()
    return


def squaremesh(x0, x1, y0, y1, r=3):
    points = np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]], dtype=np.float)
    cells = np.array([[1, 2, 0], [3, 0, 2]], dtype=np.int32)
    mesh = TriangleMesh(points, cells)
    mesh.uniform_refine(r)
    return mesh 
    

