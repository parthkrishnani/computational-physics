import numpy as np
from math import factorial
N=10000
def f(z):
    return np.exp(2*z)
i = np.arange(N)
z = np.exp(-2 * np.pi * 1j * i / N)
def df(m):
    S=0
    for k in range(N):
        S+=f(z[k])/(z[k]**(m))
    S*=factorial(m)/N
    return S.real
for m in range(6):
    print(f"df({m}) = {df(m):.6f},  exact = {2**m}")
