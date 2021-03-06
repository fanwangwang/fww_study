#定义 Point 和 Vector 类, 实现点和向量之间的运算, 如                          
# 1.point + vector 得到一个新的点                                              
# 1.vector + vector 得到一个新的向量
import numpy as np
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self,other):
        result = Point(0.0,0.0)
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result
    def __str__(self):
        return 'Point(%f,%f)'%(self.x,self.y)

class Vector(object):
    def __int__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        result = Vector(x,y)
        result = self.x + other.x
        result = self.y + other.y
        return result
    def __str__(self):
        return 'Vector([%f,%f])'%(self.x,self.y)

point1 = Point(1,2)
point2 = Point(1,5)
vector1 = Vector(1.0,2.0)
vector2 = Vector(1.0,5.0)
print(point1 - point2)

print(vector1 + vector2)


