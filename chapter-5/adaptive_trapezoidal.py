import numpy as np
def f(x):
    if x==0:
        return 1
    else:
        return ((np.sin(x))**2)/(x**2)
N=50
err=10**(-4)
def step(x1,x2):
    f1=f(x1)
    f2=f(x2)
    h=(x2-x1)/N
    I1=0.5*h*(f1+f2)
    I2=0.5*(h/2)*(f1+f2)
    for i in range(1,N):
        I1+=h*f(x1+(i*h))
    for i in range (1,2*N):
        I2+=(h/2)*f(x1+(i*(h/2)))
    if abs(I2-I1)>=3*err:
        return(step(x1,(x2/2+x1/2))+step((x2/2+x1/2),x2))
    else:
        return I2
print(step(0,10))