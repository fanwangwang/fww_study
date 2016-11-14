import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

def unique_row(a):
    tmp = np.ascontiguousarray(a).view(
            np.dtype((np.void, a.dtype.itemsize*a.shape[1])))
    _, i, j = np.unique(tmp, return_index=True, return_inverse=True)
    b = a[i, :]
    return b, i, j

class TriangleMesh:
    def __init__(self, points, cells):
        self.points = points
        self.cells = cells

    def add_plot(self, axes):
        points = self.points
        cells = self.cells
        tri = Triangulation(points[:, 0], points[:, 1], cells)
        axes.triplot(tri, 'ko-')
        axes.set_axis_off()
        axes.set_aspect('equal')

    def total_edge(self):
        points = self.points
        cells = self.cells
        NC = cells.shape[0]
        totalEdge = np.zeros((3*NC, 2), dtype=np.int)
        totalEdge[0:NC, :] = cells[:, [1, 2]]
        totalEdge[NC:2*NC, :] = cells[:, [2, 0]]
        totalEdge[2*NC:3*NC,:] = cells[:, [0, 1]]
        totalEdge.sort(axis=1)
        return totalEdge

    def auxstructure(self):
        NC = self.cells.shape[0]
        totalEdge = self.total_edge()
        edge, i, j = unique_row(totalEdge)
        cell2edge = np.reshape(j, (NC, 3), order='F')
        return edge, cell2edge

    def uniformrefine(self, n=1):
        for i in range(n):
            points = self.points
            cells = self.cells
            edge, cell2edge = self.auxstructure()
            NE = edge.shape[0]
            N = points.shape[0]
            newPoints = (points[edge[:, 0],:] + points[edge[:,1], :])/2
            self.points = np.concatenate((points, newPoints), axis=0)
            tmp = np.concatenate((cells, cell2edge + N), axis=1)
            self.cells = np.concatenate((
                tmp[:, [0, 5, 4]],
                tmp[:, [5, 1, 3]],
                tmp[:, [4, 3, 2]],
                tmp[:, [3, 4, 5]]), axis=0)
        return


def squaremesh(x0, x1, y0, y1, r=3):
    points = np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]], dtype=np.float)
    cells = np.array([[1, 2, 0], [3, 0, 2]], dtype=np.int)
    mesh = TriangleMesh(points, cells) 
    mesh.uniformrefine(r)
    return mesh 

mesh = squaremesh(-1, 1, -1, 1, 5)
f = plt.figure()
f.set_facecolor('w')
axes = f.gca()
mesh.add_plot(axes)
f.savefig('mesh.pdf')
plt.show()


