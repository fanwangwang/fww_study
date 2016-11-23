import numpy as np                                                               
t = np.linspace(0,2,20)                                                          
h = 0.1                                                                          
n = 2/h                                                                          
n = int(n)                                                                       
uh = np.zeros((n,1))                                                             
ue = np.zeros((n,1))                                                             
error = np.zeros((n,1))                                                          
uh[0] = 1                                                                        
print('隐式欧拉\t')                                                              
print('size','uh[i]','ue[i]','error[i]')                                         
for i in range(n-1):                                                             
    uh[i+1] = uh[i] + h*4*t[i]*np.sqrt(uh[i])      
    print(uh[i+1])
    uh[i+1] = uh[i] + h*4*t[i+1]*np.sqrt(uh[i+1]) 
    ue[i] = (1+t[i]*t[i])*(1+t[i]*t[i])                                          
#    error[i] = np.abs(uh[i]-ue[i])                                               
#    print(i,uh[i],ue[i],error[i])   
    error = np.sqrt(np.sum((uh[i]-ue[i])**2))                                    
    print(error) 
