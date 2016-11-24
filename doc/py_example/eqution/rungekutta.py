import numpy as np

n = 20
t = np.linspace(0,2,n)
h = 2/n
uh = np.zeros((n,1))
ue = np.zeros((n,1))
error = np.zeros((n,1))
uh[0] = 1
for i in range(n-1):
    k1 = 4*t[i]*np.sqrt(uh[i])
    k2 = 4*(t[i]+h*0.5)*np.sqrt((uh[i]+h*0.5*k1))
    k3 = 4*(t[i]+h*0.5)*np.sqrt((uh[i]+h*0.5*k2))
    k4 = 4*(t[i]+h)*np.sqrt(uh[i]+h*k3)
    uh[i+1] = uh[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    ue[i] = (1+t[i]*t[i])*(1+t[i]*t[i])
    error[i] = np.abs(uh[i] - ue[i])

error = np.max(error)
print(error)
