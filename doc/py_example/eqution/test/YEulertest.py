import numpy as np
import matplotlib.pyplot as plt 
from ODEequation import add_solution_plot,add_error_plot,ode_method_test,ODEMethod,FEuler,YEuler,IEuler,RK,XAdmas,YAdmas

def f(u, t): 
     return 4*t*np.sqrt(u)

def u(t):
    return (1 + t**2)**2

maxit = 6
n0 = 10
u0 = 1
T = [0,2]

name = 'YEuler'
method = ODEMethod(name)
uhh,tt,h,error = ode_method_test(f, u0,T, n0,u, name, maxit = 6)

ratio = error[:-1]/error[1:]
order = np.log2(ratio)

f = plt.figure(1)
axes = f.gca()
add_solution_plot(axes, u, uhh, tt)

f = plt.figure(2)
axes = f.gca()
add_error_plot(axes, h, error)
plt.show() 
print(error)
print(ratio)
print(order)
