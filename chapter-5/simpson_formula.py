import numpy as np
def f(x):
    return x**4+-2*x+1
a=0
b=2
N=100
h=(b-a)/N
I=(f(a)+f(b))
for i in range(1,N,2):
    I+=4*f(a+i*h)
for i in range(2,N,2):
    I+=2*f(a+i*h)
I=I*h/3
print(I)