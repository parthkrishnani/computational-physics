import numpy as np
def f(x):
    return x**4-2*x+1
a=0
b=2
N1=10
N2=100
h1=(b-a)/N1
h2=(b-a)/N2
I1=0.5*(f(a)+f(b))
I2=0.5*(f(a)+f(b))
for i in range(1,N1):
    I1+=f(a+i*h1)
I1*=h1
for i in range(1,N2):
    I2+=f(a+i*h2)
I2*=h2
print("Trapezoidal rule with N=10: ",I1)
print("Trapezoidal rule with N=100: ",I2)