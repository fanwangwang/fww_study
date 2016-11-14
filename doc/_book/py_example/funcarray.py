import numpy as np
def func(i,j):
        return i*j
a = np.fromfunction(func,(5,5))
print(a)
