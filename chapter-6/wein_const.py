from numpy import *
import scipy

def f(x):
    return 5*exp(-x)+x-5

x1=1
x2=10

err=1

while err>1e-6:
    f1=f(x1)
    f2=f(x2)
    x_=(x1+x2)/2
    f_=f(x_)
    if f_==0:
        break
    elif f_*f1>0:
        x1=x_
    else:
        x2=x_
    err=abs(x1-x2)

x_=0.5*(x1+x2)

print(x_)