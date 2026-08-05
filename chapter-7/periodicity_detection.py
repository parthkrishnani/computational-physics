from numpy import *
import matplotlib.pyplot as plt

data=loadtxt("chapter-7/sunspots.txt")
x=data[:,0]
y=data[:,1]
N=len(y)
def dft(y):
    c=zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            c[k]+=y[n]*exp(-1j*2*pi*k*n/N)
    return c
ck=dft(y)

coeff = abs(ck**2)

plt.plot(range(1, N//2), coeff[1:N//2])
plt.xlabel("k")
plt.ylabel("Power Spectrum")
plt.title("Power spectrum v/s k")
plt.grid()
plt.show()
