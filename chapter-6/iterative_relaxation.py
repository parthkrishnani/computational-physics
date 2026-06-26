from numpy import *
import scipy as scp

H_=1e-5

def f(c,x):
    return 1-exp(-c*x)

def d(n,u):
    return (n(u+H_)-n(u))/H_

x_=1
c_=2
err=1
iter=0

while err>10**-6:
    x1=x_
    x_=f(c_,x_)
    #print(x_)
    iter+=1
    err=abs((x_-x1)/(1-(1/d(lambda x: f(c_,x),x_))))

print(x_)
print(iter)