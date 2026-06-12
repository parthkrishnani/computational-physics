import numpy as np
from gaussxw import gaussxwab
def f(x):
    return x**3/(np.exp(x)-1)
def integrand(x):
    t=x/(1-x)
    dtdx=1/(1-x)**2
    return f(t)*dtdx
N=100
a=0
b=1
x,w=gaussxwab(N,a,b)
integral=0
for k in range(N):
    integral+=w[k]*integrand(x[k])
print("The value of the integral is:", integral)