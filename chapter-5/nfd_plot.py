import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
N=50
def C(u):
    C=0
    a=0
    b=u
    x,w=gaussxwab(N,a,b)
    for k in range(N):
        C+=w[k]*np.cos(0.5*np.pi*x[k]**2)
    return C
def S(u):
    S=0
    a=0
    b=u
    x,w=gaussxwab(N,a,b)
    for k in range(N):
        S+=w[k]*np.sin(0.5*np.pi*x[k]**2)
    return S
x=np.linspace(-5,5,200)
lam=1
z=3
u=x*np.sqrt(2/(lam*z))
def I(u):
    return 0.125*((2*C(u)+1)**2+(2*S(u)+1)**2)
I_u=np.zeros(len(x))
for i in range(len(x)):
    I_u[i]=I(u[i])
plt.plot(x,I_u)
plt.xlabel('x')
plt.ylabel('Intensity')
plt.title('Diffraction Pattern')
plt.grid()
plt.show()