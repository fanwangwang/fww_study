import numpy as np     
import matplotlib.pyplot as plt
n = 10
t = np.linspace(0,2,n+1)                                                          
h = 2/n                                                                          
uh = np.zeros((n+1,1))                                                             
ue = np.zeros((n+1,1))                                                             
error = np.zeros((n+1,1))                                                          
uh[0] = 1                                                                        
print('改进欧拉')
for i in range(n):                                                             
    uh[i+1] = uh[i] + h*4*t[i]*np.sqrt(uh[i])                                    
    uh[i+1] = uh[i] + h*0.5*(4*t[i]*np.sqrt(uh[i])+4*t[i+1]*np.sqrt(uh[i+1]))
    ue[0] = (1+t[0]*t[0])*(1+t[0]*t[0]) 
    ue[i+1] = (1+t[i+1]*t[i+1])*(1+t[i+1]*t[i+1])                                          
    error[i] = np.abs(uh[i]-ue[i]) 

error = np.max(error)
print(error)

plt.plot(t,uh,label = "numberical solution",color = "red")
plt.plot(t,ue,label = "exact solution" ,color = "blue")

plt.xlabel("t")
plt.ylabel("u")
plt.title("improve euler")
plt.legend()
plt.savefig("imeuler.pdf")

plt.show()
