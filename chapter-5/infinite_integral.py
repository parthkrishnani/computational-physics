import numpy as np
from gaussxw import gaussxwab
N=50
def f(x):
    return np.exp(-np.tan(x)**2)*(1/np.cos(x)**2)
a=0
b=np.pi/2
x,w=gaussxwab(N,a,b)
integral=0
for k in range(N):
    integral+=w[k]*f(x[k])
print("The value of the integral is:", integral)
