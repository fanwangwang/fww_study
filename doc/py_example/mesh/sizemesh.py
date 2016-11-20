import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

points = np.array([[0,0],[1,0],[1,1],[0,1]],dtype = np.float)
h = 0.5
n = 1/h
n = int(n)
print(n)
for i in range(n+1):
    for j in range(n+1):
        points = np.array([[i*h,j*h]],dtype = np.float)
        cells = np.array([[i+j*(n+1),i+1+j*(n+1),i+(j+1)*(n+1)],[
            i+1+(j+1)*(n+1),i+(j+1)*(n+1),(i+1)+j*(n+1)]],dtype = np.int)
        print(points)
        print(cells)
f = plt.figure()
axes = f.gca()
tri = Triangulation(points[:,0],points[:,1],cells)
axes.triplot(tri,'-ko')
plt.show()
