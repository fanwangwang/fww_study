import numpy as np                                                              
import matplotlib.pyplot as plt

def add_solution_plot(axes, u, uhh, tt):
    '''
    This function is a make figure of numberical solution and exact solution!
    '''
    ue = u(tt[-1])
    axes.plot(tt[-1], ue, '-r', label="The true solution", color='k')
    for j in range(len(tt)):
        axes.plot(tt[j], uhh[j], '--r', label = "$u_"+str(j)+"$")

def add_error_plot(axes, h, error):
    '''
    This function is a make figure for order of  error!
    '''
    axes.loglog(h, error, '-*r')

def ODEMethod(mname):
    '''
    This function is choosed a method of ODE eqution
    '''
    if mname is 'FEuler':
        return FEuler
    elif mname is 'YEuler':
        return YEuler
    elif mname is 'IEuler':
        return IEuler
    elif mname is 'RK':
        return RK
    elif mname is 'XAdmas':
        return XAdmas
    elif mname is 'YAdmas':
        return YAdmas
    else:
        return

def ode_method_test(f, u0, T, n0, u, name='FEuler', maxit = 4):
    '''
    This function is resolve the numberical solution and error!
    Maxit is number of iterations!
    '''
    error = np.zeros(maxit)
    h = np.zeros(maxit)
    method = ODEMethod(name)
    uhh = []
    tt = []
    for j in range(maxit):
        uh, t, h[j] = method(f, u0, T, n0*2**j)
        ue =u(t)
        error[j] = np.abs(uh-ue).max()
        uhh.append(uh)
        tt.append(t)
    return uhh, tt, h, error

def FEuler(f, u0, T, n):    
    '''
    This method is expilict euler,and its form is:
    u[n+1] = u0 + h*f(tn,un)
    '''                                                    
    uh = np.zeros(n+1)                                                          
    t = np.linspace(T[0], T[1], n+1)                                                  
    uh[0] = u0                                                                  
    dt = (T[1] -T[0])/n             
    for i in range(n):                                                           
        uh[i+1] = uh[i] + dt*f(uh[i], t[i])                                      
    return uh, t, dt


def YEuler(f, u0, T, n):
    '''
    This method is impilict euler,and its form is: 
    u[n+1] = u0 + h*f(t[n+1],u[n+1])
    '''
    uh = np.zeros(n+1)                                                          
    t = np.linspace(T[0],T[1],n+1)                                                  
    uh[0] = u0                                                                  
    dt = (T[1] - T[0])/n             
    for i in range(n):                                                           
        uh[i+1] = uh[i] + dt*f(uh[i],t[i])
        tmp = uh[i+1]
        j = 0                                                                       
        while j<11:                                                                 
            j = j+1                                                                 
            uh[i+1] = uh[i] + dt*f(uh[i+1],t[i+1])
            f1 = f(uh[i+1],t[i+1])
            uh[i+1] = uh[i] + dt*f1
            if np.abs(tmp - uh[i+1]) < 1e-12:                                       
                break                                                               
    return uh, t, dt


def IEuler(f, u0, T, n):
    '''
    This method is improve euler,and its form is:
    u[n+1] = u0 + h*(f(tn,un)+f(t[n+1],u[n+1]))
    '''
    uh = np.zeros(n+1)
    t = np.linspace(T[0],T[1],n+1)
    uh[0] = u0
    dt = (T[1]-T[0])/n
    for i in range(n):
        uh[i+1] = uh[i] + dt*f(uh[i],t[i])
        tmp = uh[i+1]
        j = 0 
        while j<11:
            j = j+1
            uh[i+1] = uh[i] + 0.5*dt*(f(uh[i],t[i]) + f(uh[i + 1],t[i + 1]))
            if np.abs(tmp - uh[i+1]) < 1e-12:
                break
    return uh, t, dt

def RK(f, u0, T, n):
    '''
    This method is runge kutta,and its form is:
    k1 = f(u[n], t[n])
    k2 = f(u[n] + 0.5*h*k1, t[n] + 0.5*h)
    k3 = f(u[n] + 0.5*h*k2, t[h] + 0.5*h)
    k4 = f(u[n] + h*k3, t[n] + h)
    u[n+1] = u[n] + h*(k1 + 2*k2 + 2*k3 + k4)/6

    '''
    uh = np.zeros(n+1)
    t = np.linspace(T[0], T[1], n+1)
    uh[0] = u0
    dt = (T[1]-T[0])/n
    for i in range(n):
        k1 = f(uh[i], t[i])
        k2 = f(uh[i] + 0.5*dt*k1, t[i] + 0.5*dt)
        k3 = f(uh[i] + 0.5*dt*k2, t[i] + 0.5*dt)
        k4 = f(uh[i] + dt*k3, t[i] + dt)
        uh[i+1] = uh[i] + dt*(k1 + 2*k2 + 2*k3 + k4)/6
    return uh, t, dt

def XAdmas(f,u0,T,n):
    '''
    This method is expilict admas,and its form is:
    u[n+1] = u[n] + h*(55*f(u[n],t[n]) -59*f(u[n-1],t[n-1])
    +37*f(u[n-2],t[n-2])-9*f(u[n-3],t[n-3]))/24 
    '''
    uh = np.zeros(n+1)
    t = np.linspace(T[0],T[1],n+1)
    uh[0] = u0
    dt = (T[1]-T[0])/n
    for i in range(3):
        k1 = f(uh[i],t[i])
        k2 = f(uh[i] + 0.5*dt*k1, t[i] + 0.5*dt)
        k3 = f(uh[i] + 0.5*dt*k2, t[i] + 0.5*dt)
        k4 = f(uh[i] + dt*k3, t[i] + dt)
        uh[i+1] = uh[i] + dt*(k1 + 2*k2 + 2*k3 + k4)/6
    for i in range(3,n):
        uh[i+1] = uh[i] + dt*(55*f(uh[i],t[i]) -59*f(uh[i-1],t[i-1])
        +37*f(uh[i-2],t[i-2])-9*f(uh[i-3],t[i-3]))/24
    return uh, t, dt

def YAdmas(f,u0,T,n):
    '''
    This method is impilict admas,and its form is:
    u[n+1] = u[n] +h/24*(9*f(t[n+1],uh[n+1])+19*f(t[n],uh[n])
    -5*f(t[n-1],uh[n-1])+f(t[n-2],uh[n-2])

    '''

    uh = np.zeros(n+1)
    t = np.linspace(T[0],T[1],n+1)
    uh[0] = u0
    dt = (T[1]-T[0])/n
    for i in range(3):
        k1 = f(uh[i],t[i])                                                      
        k2 = f(uh[i] + 0.5*dt*k1, t[i] + 0.5*dt)                                
        k3 = f(uh[i] + 0.5*dt*k2, t[i] + 0.5*dt)                                
        k4 = f(uh[i] + dt*k3, t[i] + dt)                                        
        uh[i+1] = uh[i] + dt*(k1 + 2*k2 + 2*k3 + k4)/6                          
    for i in range(3,n):
        uh[i+1] = uh[i] + dt*(55*f(uh[i],t[i]) -59*f(uh[i-1],t[i-1])            
        +37*f(uh[i-2],t[i-2])-9*f(uh[i-3],t[i-3]))/24 
        tmp = uh[i+1]                                                           
        j = 0                                                                   
        while j<11:  
            j = j+1 
            uh[i+1] = uh[i] + dt/24*(9*f(t[i+1],uh[i+1])+19*f(t[i],uh[i])
            -5*f(t[i-1],uh[i-1])+f(t[i-2],uh[i-2]))                
            if np.abs(tmp - uh[i+1]) < 1e-12:
                break
    return uh,t, dt
