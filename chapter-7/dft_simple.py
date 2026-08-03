from numpy import *
import matplotlib.pyplot as plt

N=1000
n=linspace(1,1000,N)
yn=sin(pi*n/N)*sin(20*pi*n/N)

def dft(y):
    c=zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            c[k]+=y[n]*exp(-1j*2*pi*k*n/N)
    return c

k = arange(N)
plt.plot(k, abs(dft(yn)))
plt.grid()
plt.show()