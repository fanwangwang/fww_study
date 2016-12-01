import numpy as np                                                              

def f(ti, ui):
    return 4*ti*np.sqrt(ui)

def u(t):
    return (1+t*t)**2

n = 80                                    
t = np.linspace(0,2,n+1)                                                        
h = 2/n                                                                         
uh = np.zeros((n+1,))                                                          
uh[0] = 1                                                                       
for i in range(3):
    k1 = 4*t[i]*np.sqrt(uh[i])                                                  
    k2 = 4*(t[i]+h*0.5)*np.sqrt((uh[i]+h*0.5*k1))                               
    k3 = 4*(t[i]+h*0.5)*np.sqrt((uh[i]+h*0.5*k2))                               
    k4 = 4*(t[i]+h)*np.sqrt(uh[i]+h*k3)                                         
    uh[i+1] = uh[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6 

for i in range(3, n):                                                              
    uh[i+1] = uh[i] + h/24*(55*f(t[i], uh[i]) -59*f(t[i-1], uh[i-1])+37*f(t[i-2], uh[i-2])-9*f(t[i-3],uh[i-3]))

ue = u(t)
error = np.max(np.abs(uh - ue))                                                           
print(error)       
