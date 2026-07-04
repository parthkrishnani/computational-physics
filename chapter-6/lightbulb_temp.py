import numpy as np
import matplotlib.pyplot as plt


lam1=390e-9
lam2=750e-9
h=6.626e-34
c=3e8
kb=1.38e-23

def integrand(x):
    return x**3/(np.exp(x)-1)

def n(T):
    a=h*c/(lam2*kb*T)
    b=h*c/(lam1*kb*T)
    xx,ww=np.polynomial.legendre.leggauss(100)
    t=0.5*(b-a)*xx+0.5*(b+a)
    I=0.5*(b-a)*np.dot(ww,integrand(t))
    
    return I*15/(np.pi)**4

x_val = np.linspace(300,10000,10000)
n_val = np.array([n(T) for T in x_val])

plt.plot(x_val,n_val)
plt.xlabel("T(K)")
plt.ylabel("n(T)")
plt.title("Efficiency of an incandescant lightbulb v/s Operation Temperature")
plt.grid()
plt.show()