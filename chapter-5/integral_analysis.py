import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-x**2)
x_val=np.arange(0,3.1,0.1)
x_plt=[]
E_plt=[]
for x in x_val:
    a=0
    b=x
    N=100
    h=(b-a)/N
    I=(f(a)+f(b))
    for i in range(1,N,2):
        I+=4*f(a+i*h)
    for i in range(2,N,2):
        I+=2*f(a+i*h)
    I=I*h/3
    x_plt.append(x)
    E_plt.append(I)
plt.plot(x_plt,E_plt)
plt.xlabel('x')
plt.ylabel('Integral of exp(-x^2) from 0 to x')
plt.title('Integral of exp(-x^2) using Simpson\'s rule')
plt.grid()
plt.show()