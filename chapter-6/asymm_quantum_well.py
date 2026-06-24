from numpy import *
from scipy import *
from scipy.integrate import quad

H_ = 1e-5
L = 1.0
a = 1e-2
h = 6.626e-34
hbar = h / (2*pi)    
M = 1.6e-31

def d(n,u):
    return (n(u+H_)-n(u))/H_
def v(x):
    return a*x/L
def psi(n, x):
    return sin(pi * n * x / L)
def f(x,m,n):
    d2psi = d(lambda u: d(lambda u: psi(n, u), u), x)
    k1 = -hbar**2 * d2psi / (2*M)
    k2 = v(x) * psi(n, x)
    return psi(m, x) * (k1 + k2)

N=10
H=zeros([N,N], float)

for i in range(N):
    for j in range(N):
        H[i,j]=(2*quad(lambda p: f(p,i+1,j+1),0,L)[0])/L

print(H)

vals, vecs = linalg.eigh(H)

print("Eigenvalues:",vals)
print("Eigenstates:",vecs)