import numpy as np
import matplotlib.pyplot as plt
def f(m,t,x):
    return np.cos(m*t-x*np.sin(t))
a=0
b=np.pi
N=1000
h=(b-a)/N
m=1
x_val=np.arange(0,20.1,0.1)
x_plt=[]
f_plt=[]
for x in x_val:
    I=(f(m,a,x)+f(m,b,x))
    for i in range(1,N,2):
        I+=4*f(m,a+i*h,x)
    for i in range(2,N,2):
        I+=2*f(m,a+i*h,x)
    I=I*h/3
    x_plt.append(x)
    f_plt.append((I/x)**2)
plt.plot(x_plt,f_plt)

m=2
x_val=np.arange(0,20.1,0.1)
x_plt=[]
f_plt=[]
for x in x_val:
    I=(f(m,a,x)+f(m,b,x))
    for i in range(1,N,2):
        I+=4*f(m,a+i*h,x)
    for i in range(2,N,2):
        I+=2*f(m,a+i*h,x)
    I=I*h/3
    x_plt.append(x)
    f_plt.append((I/x)**2)

plt.plot(x_plt,f_plt)

m=0
x_val=np.arange(0,20.1,0.1)
x_plt=[]
f_plt=[]
for x in x_val:
    I=(f(m,a,x)+f(m,b,x))
    for i in range(1,N,2):
        I+=4*f(m,a+i*h,x)
    for i in range(2,N,2):
        I+=2*f(m,a+i*h,x)
    I=I*h/3
    x_plt.append(x)
    f_plt.append((I/x)**2)
plt.plot(x_plt,f_plt)
plt.show()