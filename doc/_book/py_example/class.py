class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        result = Point(0,0)
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result
    def magnitude(self):
        return(self.x**2 + self.y**2)**0.5
    def __str__(self):
        return 'Point(%f,%f)'%(self.x,self.y)

point1 = Point(5,10)
point2 = Point(6,15)
print(point1)
print(point2)
print(point1 + point2)
print(point1 + point2)
print(point1.magnitude())
