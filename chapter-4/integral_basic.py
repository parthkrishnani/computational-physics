import numpy as np
def y(x):
    return np.sqrt(1-x**2)
N=1000
h=2/N
I=0
for k in range(N):
    xk=-1+k*h
    yk=y(xk)
    I+=h*yk
print(I)