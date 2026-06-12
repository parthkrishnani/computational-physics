import numpy as np
from math import factorial
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
def H(n, x):
    h = np.zeros(n+1)
    h[0] = 1
    if n == 0:
        return h[0]
    h[1] = 2*x
    for k in range(2, n+1):
        h[k] = 2*x*h[k-1] - 2*(k-1)*h[k-2]
    return h[n]
def psi(n,x):
    return 1/np.sqrt(2**n*factorial(n)*np.sqrt(np.pi))*H(n,x)*np.exp(-x**2/2)
x=np.linspace(-5,5,1000)
p0=np.zeros(len(x))
p1=np.zeros(len(x))
p2=np.zeros(len(x))
p3=np.zeros(len(x))
for i in range(len(x)):
    p0[i]=psi(0,x[i])
    p1[i]=psi(1,x[i])
    p2[i]=psi(2,x[i])
    p3[i]=psi(3,x[i])

plt.plot(x,p0,label='n=0')
plt.plot(x,p1,label='n=1')
plt.plot(x,p2,label='n=2')
plt.plot(x,p3,label='n=3')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid()
#plt.show()
x_=np.linspace(-10,10,1000)
p30=np.zeros(len(x_))
for i in range(len(x_)):
    p30[i]=psi(30,x_[i])
plt.plot(x_,p30,label='n=30')
plt.show()

def integrand(x):
    t=x/(1-x)
    dt_dx=1/(1-x)**2
    return (t)**2*psi(5,t)**2*dt_dx
N=50
x, w = gaussxwab(N, 0, 1)
integral = 2 * sum(w[k] * integrand(x[k]) for k in range(N))
print("The value of the uncertainty is:", np.sqrt(integral))