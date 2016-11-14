import numpy as np          #调用"numpy"模块命名"np"
from scipy.sparse import csc_matrix, csr_matrix, spdiags, eye
        
       # 从scipy.sparse调用按列,行存储的矩阵,对角矩阵,单位矩阵
        
from scipy.sparse import triu, tril, find, hstack
        
       # 从scipy.sparse调用上三角,下三角矩阵,find, hstack
        

from matplotlib.tri import Triangulation
        
       # 从matplotlib.tri调用Triangulation(三角形剖分)
        
from tool import unique_row



class Mesh:             #定义一个网格类(单元和节点)
    """
    
    """
    def __init__(self, points, cells):      #定义节点和单元
        """ Constructor
        INPUT:
            points: array object, N*dim matrix, the node coordinates 
            cells: array object, NT*n matrix,  NT elems with n nodes 
        """
        self.points = points 
        self.cells = cells 
    
    def number_of_points(self):             #定义点的总数
        """ The number of points
        """
        return self.points.shape[0]

    def number_of_cells(self):              #定义单元的总数
        """ The number of cells
        """
        return self.cells.shape[0]

    def geom_dimentsion(self):              #定义几何的维数
        """ The geometric dimension of the mesh
        """ 
        return self.points.shape[1]

    def __str__(self):                      #定义函数返回点和单元
        print("Ponts: ")
        print(self.points)
        print("Cells: ")
        print(self.cells)

class TriangleMesh(Mesh):                   #继承Mesh类的三角形网格类
    """
    Example:
        points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float)
        cells = np.array([[1, 2, 0], [3, 0, 2]], dtype=np.int32)
        mesh = TriangleMesh(points, cells)
    """
    def __init__(self, points, cells):      #调用Mesh类初始化函数
        """ Constructor
        INPUT:
            points: array object, N*dim matrix, the node coordinates 
            cells: array object, NT*3 matrix,  NT triangle mesh
        """
        Mesh.__init__(self, points, cells)        

    def total_edge(self):                   #总的边数
        NC = self.cells.shape[0]
        totalEdge = np.zeros((3*NC, 2), dtype=np.int)
        n = [1, 2, 0]
        p = [2, 0, 1]
        for i in range(3):
            j = i+1
            idx = np.arange(i*NC, j*NC)
            totalEdge[idx, :] = self.cells[:, [n[i], p[i]]]
        totalEdge.sort(axis=1)              #总的边数按列排序
        return totalEdge

    def auxstructure(self):
        totalEdge = self.total_edge()
        edge, i, j = unique_row(totalEdge)      #处理行相同的边
        NT = self.cells.shape[0]                #单元的个数，即矩阵的行数
        cell2edge = np.reshape(j, (NT, 3), order='F')       
                        #把edge变成一个NT×3的列向量，F：隔NT行取一个元素
        return (edge, cell2edge)

    def is_boundary_node(self):                 #边界上的节点
        N = self.points.shape[0]
        NC = self.cells.shape[0]
        totalEdge = self.total_edge()            #总的边
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

    def uniform_refine(self, n=1):      #加密网格
        for i in range(n):
            N = self.points.shape[0]    #节点总数
            NC = self.cells.shape[0]
            edge, cell2edge = self.auxstructure()
            NE = edge.shape[0]          #边的总数，按行排列

            edge2newPoints = np.arange(N, N+NE)     #增加的NE个新点

            newPoints = (self.points[edge[:, 0], :] + self.points[edge[:, 1],
                :])/2.0;        #新点，每个边的中点
            self.points = np.concatenate((self.points, newPoints))
                            #拼接原来的点与新的点
            p = np.concatenate((self.cells, edge2newPoints[cell2edge]), axis=1)
            self.cells = np.concatenate((
                p[:, [0, 5, 4]], 
                p[:, [5, 1, 3]],
                p[:, [4, 3, 2]],
                p[:, [3, 4, 5]]))
        return

    def grad_lambda(self):      #求重心坐标
        NT = self.number_of_cells()     #单元个数
        points = self.points
        cells = self.cells
        v0 = points[cells[:, 2], :] - points[cells[:, 1], :]
        #所有单元的第二个顶点减去第一个顶点，即2号顶点与1号顶点的边
        v1 = points[cells[:, 0], :] - points[cells[:, 2], :]
        v2 = points[cells[:, 1], :] - points[cells[:, 0], :]

        area = 0.5*(-v2[:, [0]]*v1[:, [1]] + v2[:, [1]]*v1[:, [0]])
        Dlambda0 = np.concatenate((-v0[:,[1]], v0[:, [0]]), axis=1)/(2*area)
        #按逆时针旋转90度
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

def showmesh(mesh, ax):         #显示出网格的图
    tri = Triangulation(mesh.points[:, 0], mesh.points[:, 1], mesh.cells)
    ax.set_aspect('equal')      #坐标比例相同
    ax.triplot(tri)             #作出tri的图
    ax.set_axis_off()           #去除坐标轴
    return


def squaremesh(x0, x1, y0, y1, r=3):         #作四边形网格
    points = np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]], dtype=np.float)
    cells = np.array([[1, 2, 0], [3, 0, 2]], dtype=np.int32)
    mesh = TriangleMesh(points, cells)
    mesh.uniform_refine(r)
    return mesh 
    

