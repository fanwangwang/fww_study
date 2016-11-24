import numpy as np

n = 80
t = np.linspace(0,2,n)
h = 2/n
uh = np.zeros((n,1))
ue = np.zeros((n,1))
error = np.zeros((n,1))
uh[0] = 1
print('显示欧拉\t')
print('size','uh[i]','ue[i]','error[i]')
for i in range(n-1):
    uh[i+1] = uh[i] + h*4*t[i]*np.sqrt(uh[i])
    ue[i] = (1+t[i]*t[i])*(1+t[i]*t[i])
    error[i] = np.abs(uh[i]-ue[i])

error = np.max(error)
print(error)



