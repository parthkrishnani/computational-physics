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
w=0.5
iter=0

while err>10**-6:
    iter+=1
    x1=x_
    x_=(1+w)*f(x_,c_)-w*x_
    err=abs((x_-x1)/(1-(1/((1+w)*d(lambda x: f(c_,x),x_)-w))))

print(iter)
print(x_)