import numpy as np       
import matplotlib.pyplot as plt
n = 320
t = np.linspace(0,2,n+1)                                                          
h = 2/n                                                                          
uh = np.zeros((n+1,))                                                             
ue = np.zeros((n+1,))                                                             
error = np.zeros((n+1,))                                                          
uh[0] = 1                                                                        
ue[0] = (1+t[0]*t[0])*(1+t[0]*t[0])                                          
print('隐式欧拉\t')                                                              
for i in range(n):    
    uh[i+1] = uh[i] + h*4*t[i]*np.sqrt(uh[i])
    tmp = uh[i+1]
    j = 0
    while j<11:
        j = j+1
        uh[i+1] = uh[i] + h*4*t[i+1]*np.sqrt(uh[i+1]) 
        f1 = 4*t[i+1]*np.sqrt(uh[i+1])
        uh[i+1] = uh[i] + h*f1
        f2 = 4*t[i+1]*np.sqrt(uh[i+1])
        uh[i+1] = uh[i] + h*f2
        if np.abs(tmp - uh[i+1]) < 1e-12:
            break
        tmp = uh[i+1]
    ue[i+1] = (1+t[i+1]*t[i+1])*(1+t[i+1]*t[i+1])                                          
    error[i] = np.abs(uh[i]-ue[i])      
error = np.max(error)
print(error)


plt.plot(t,uh,label = "numberical solution",color = "red")
plt.plot(t,ue,label = "exact solution",color = "blue")

plt.xlabel("t")
plt.ylabel("u")
plt.title("implicit euler")
plt.legend()
plt.savefig("implicit.pdf")
plt.show()
