import numpy as np
def y(x):
    return x**4+2*x+1
N=1000
a=0.0
b=2.0
h=(b-a)/N
I=0.5*(y(a)+y(b))
for k in range(1,N):
    I+=y(a+k*h)
I*=h
print(I)