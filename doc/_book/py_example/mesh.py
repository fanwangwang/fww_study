import numpy as np      #调用nump模块，并简写为np
from scipy.sparse import csc_matrix, csr_matrix, spdiags, eye
                        #从scipy.sparse模块中调用csc_matrix,csr_matrix,spdiags,eye
from scipy.sparse import triu, tril, find, hstack

from matplotlib.tri import Triangulation


def unique_row(a): 
    tmp = np.ascontiguousarray(a).view(np.dtype((np.void,
        a.dtype.itemsize * a.shape[1])))
    _, i, j = np.unique(tmp, return_index=True,
            return_inverse=True)
    b = a[i]
    return (b, i, j)



class Mesh:             #定义一个网格类（单元和节点）
    def __init__(self, points, cells):  #初始化
        """ Constructor
        INPUT:
            points: array object, N*dim matrix, the node coordinates 
            cells: array object, NT*n matrix,  NT elems with n nodes 
        """
        self.points = points 
        self.cells = cells 
    
    def number_of_points(self):         #定义节点的总数
        """ The number of points
        """
        return self.points.shape[0]

    def number_of_cells(self):          #定义单元的总数
        """ The number of cells
        """
        return self.cells.shape[0]

    def geom_dimentsion(self):          #定义几何的维数
        """ The geometric dimension of the mesh
        """ 
        return self.points.shape[1]

    def __str__(self):                  #定义函数返回点和单元
        print("Ponts: ")
        print(self.points)
        print("Cells: ")
        print(self.cells)

class TriangleMesh(Mesh):               #继承Mesh类的三角形网格类
    def __init__(self, points, cells):  #调用Mesh类初始化函数
        """ Constructor
        INPUT:
            points: array object, N*dim matrix, the node coordinates 
            cells: array object, NT*3 matrix,  NT triangle mesh
            每个三角形有三个节点，NT个三角形网格
        """
        Mesh.__init__(self, points, cells)        

    def auxstructure(self):
        edge0 = self.cells[:, [1, 2]]   #每个单元的第0号边，即节点[1,2]对应的边
        edge1 = self.cells[:, [2, 0]]
        edge2 = self.cells[:, [0, 1]]
        totalEdge = np.concatenate((edge0, edge1, edge2))
                                        #把三个边拼接起来，返回总的边数
        totalEdge.sort(axis=1)          #总的边数按列排序
        edge, i, j = unique_row(totalEdge)
        NT = self.cells.shape[0]        #单元的个数，即矩阵的行数
        cell2edge = np.reshape(j, (NT, 3), order='F')
                                        #把edge变成一个NT×3的列向量，F：隔NT行取一个元素
        return (edge, cell2edge)

    def uniform_refine(self, n=1):      #加密网格
        for i in range(n):              
            N = self.number_of_points() #节点总数
            NT = self.number_of_cells() #单元总数
            edge, cell2edge = self.auxstructure()#
            NE = edge.shape[0]          #边的总数，按行排列

            edge2newPoints = np.arange(N, N+NE)#增加的NE个新点

            newPoints = (self.points[edge[:, 0], :] + self.points[edge[:, 1],
                :])/2.0;    #新点，每个边的中点
            self.points = np.concatenate((self.points, newPoints))
                            #拼接原来的点与新的点
            p = np.concatenate((self.cells, edge2newPoints[cell2edge]), axis=1)

            self.cells = np.concatenate((
                p[:, [0, 5, 4]], 
                p[:, [5, 1, 3]],
                p[:, [4, 3, 2]],
                p[:, [3, 4, 5]]))
        return


    

def showmesh(mesh, ax):                 #显示出网格的图
    tri = Triangulation(mesh.points[:, 0], mesh.points[:, 1], mesh.cells)
    ax.set_aspect('equal')              #坐标比例相同
    ax.triplot(tri)                     #作出tri的图
    ax.set_axis_off()                   #去除坐标轴
    return


def squaremesh(x0, x1, y0, y1):         #作四边形网格
    points = np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]], dtype=np.float)
                                        #调用nump模块下的数组array生成四个顶点
    cells = np.array([[1, 2, 0], [3, 0, 2]], dtype=np.int32)
                                        #调用nump模块下的数组array生成单元，指定类型存储
    return TriangleMesh(points, cells)  #返回三角形网格

    

