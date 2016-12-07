import numpy as np

def f(a,b,c):
    s = b**2-4*a*c
    if s > 0:
        print('The equation has two different roots!')
        x1 = (-b+np.sqrt(s))/(2*a)
        x2 = (-b-np.sqrt(s))/(2*a)
        print(x1,x2)
    elif s == 0:
        print('The equation has two same roots!')
        x1 = (-b+np.sqrt(s))/(2*a)
        x2 = (-b-np.sqrt(s))/(2*a)
        print(x1,x2)
    else:
        print('The equation has not roots!')



a = 1
b = 2
c = 4
print(f(a,b,c))
