import numpy as np
def f(x):
    return x**4-2*x+1
h_der=10**(-5)
def df(x):
    return (f(x+h_der)-f(x))/h_der
a=0
b=2
N=10
h_int=(b-a)/N
I=0.5*h_int*(f(a)+f(b))+h_int**2*(df(a)-df(b))/12
for k in range(1,N):
    I+=h_int*(f(a+k*h_int))
print(I)