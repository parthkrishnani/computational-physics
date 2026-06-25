from numpy import *
import scipy as scp
import matplotlib.pyplot as plt

H_=1e-5

def f(c,x):
    return 1-exp(-c*x)

def d(n,u):
    return (n(u+H_)-n(u))/H_

x_lin=[]
c_lin = linspace(0,3,4000)

for c in c_lin:
    err=1
    x_=1
    while err>10**-6:
        x1=x_
        x_=f(c,x_)
        df = d(lambda x: f(c,x),x_)
        if df!=0:
            err=abs((x_-x1)/(1-(1/df)))
        else:
            break
    x_lin.append(x_)

plt.plot(c_lin,x_lin)
plt.grid()
plt.xlabel("c")
plt.ylabel("x(c)")
plt.title("Percolation Transition Plot")
plt.show()