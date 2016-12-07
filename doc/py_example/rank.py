
def f(x,y,z):
    '''
    给出三个数比较大小
    '''
    
    if x>y:
        if x>z:
            return x
        else:
            return z
    else:
        if y>z:
            return y
        else:
            return z
x = 5
y = 2
z = 0
print(f(x,y,z))
