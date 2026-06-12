import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
def f(x):
    return np.tan(x)**3/(np.cos(x)**2*(np.exp(np.tan(x))-1))
N=100
a=0
b=np.pi/2
x,w=gaussxwab(N,a,b)
integral=0
for k in range(N):
    integral+=w[k]*f(x[k])
print("The value of the integral is:", integral)