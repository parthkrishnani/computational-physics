import numpy as np
from gaussxw import gaussxwab
V=10**(-3)
rho=6.022*10**28
theta_d=428
N=50
kb=1.38064852*10**(-23)
def cv(T):
    S=0
    a=0
    b=theta_d/T
    x,w=gaussxwab(N,a,b)
    for k in range(N):
        S+=w[k]*x[k]**4*np.exp(x[k])/(np.exp(x[k])-1)**2
    return 9*V*rho*kb*(T/theta_d)**3*S
T=np.linspace(5,500,100)
C_v=np.zeros(len(T))
for i in range(len(T)):
    C_v[i]=cv(T[i])
import matplotlib.pyplot as plt
plt.plot(T,C_v)
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity (J/K)')
plt.title('Debye Heat Capacity')
plt.grid()
plt.show()    