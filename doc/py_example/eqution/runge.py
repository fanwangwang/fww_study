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
    k2 = 4*(t[i]+h/3)*np.sqrt(uh[i]+h*k1/3)
    k3 = 4*(t[i]+2*h/3)*np.sqrt(uh[i]-h*k1/3+h*k2)
    k4 = 4*(t[i]+h)*np.sqrt(uh[i]+h*k1-h*k2+h*k3)
    uh[i+1] = uh[i] + h*(k1+3*k2+3*k3+k4)/8
    ue[i] = (1+t[i]*t[i])*(1+t[i]*t[i])
    error[i] = np.abs(uh[i] - ue[i])
    print(ue[i],uh[i])
error = np.max(error)
print(error)

