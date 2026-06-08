import numpy as np
def f(x):
    return np.sin(10*np.sqrt(x))**2
a=0
b=1
M=10
N=np.zeros(M)
for i in range(M):
    N[i]=2**i
h=np.zeros(M)
for i in range(M):
    h[i]=(b-a)/N[i]
S=np.zeros(M)
for i in range(M):
    S[i]=(f(a)+f(b))/3
    for j in range(2,int(N[i]),2):
        S[i]+=2*f(a+j*h[i])/3
T=np.zeros(M)
for i in range(M):
    for j in range(1,int(N[i]),2):
        T[i]+=4*f(a+j*h[i])/3
I=np.zeros(M)
for i in range(M):
    I[i]=h[i]*(S[i]+T[i])
print(I)