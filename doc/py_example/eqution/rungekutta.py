import numpy as np
import matplotlib.pyplot as plt
n = 160
t = np.linspace(0,2,n+1)
h = 2/n
uh = np.zeros((n+1,1))
ue = np.zeros((n+1,1))
error = np.zeros((n+1,1))
uh[0] = 1
for i in range(n):
    k1 = 4*t[i]*np.sqrt(uh[i])
    k2 = 4*(t[i]+h*0.5)*np.sqrt((uh[i]+h*0.5*k1))
    k3 = 4*(t[i]+h*0.5)*np.sqrt((uh[i]+h*0.5*k2))
    k4 = 4*(t[i]+h)*np.sqrt(uh[i]+h*k3)
    uh[i+1] = uh[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    ue[0] = (1+t[0]*t[0])*(1+t[0]*t[0])
    ue[i+1] = (1+t[i+1]*t[i+1])*(1+t[i+1]*t[i+1])
    error[i] = np.abs(uh[i] - ue[i])

error = np.max(error)
print(error)


plt.plot(t,uh,label = "numberical solution",color = "red")                      
plt.plot(t,ue,label = "exact solution",color = "blue")                          
                                                                           
plt.xlabel("t")                                                                 
plt.ylabel("u")                                                                 
plt.title("rungekutta method")                                                       
plt.legend()                                                                    
plt.show()
