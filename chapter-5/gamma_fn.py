import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
def integrand(x,a):
    return x**(a-1)*np.e**(-x)
def gamma(a):
    lo=0
    hi=1
    N=50
    z,w=gaussxwab(N,lo,hi)
    c=a-1
    x = c*z/(1-z)
    I=integrand(x,a)
    dzdx=c/((1-z))**2
    I*=dzdx
    Integ=0
    for j in range(N):
        Integ+=w[j]*I[j]
    return Integ
    

    
x_=np.linspace(0,5,1000)
plt.plot(x_, integrand(x_, 1), label="a=1")
plt.plot(x_, integrand(x_, 2), label="a=2")
plt.plot(x_, integrand(x_, 3), label="a=3")
plt.plot(x_, integrand(x_, 4), label="a=4")
plt.grid()
plt.xlabel("x")
plt.ylabel("Integrand")
plt.title("Plot of the Integrand against x for varying values of a")
plt.legend()
plt.show()

x_ = np.linspace(0.1,10,100)
y_ = [gamma(a) for a in x_]

plt.plot(x_, y_)
plt.xlabel("a")
plt.ylabel("gamma(a)")
plt.title("Gamma(a) v/s a")
plt.show()

