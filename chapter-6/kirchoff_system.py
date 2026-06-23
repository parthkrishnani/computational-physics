from numpy import *
from scipy import linalg
N=10000
v=zeros([N],float)
b=zeros([N],float)
v0=5
b[0]=v0
b[1]=v0
A = zeros([5, N], float)
A[0, 2:]   = -1    # second upper diagonal
A[1, 1:]   = -1    # first upper diagonal
A[2, :]    =  4    # main diagonal
A[2, 0]    =  3    # corner modification
A[2, N-1]  =  3    # corner modification
A[3, :N-1] = -1    # first lower diagonal
A[4, :N-2] = -1    # second lower diagonal
v=linalg.solve_banded((2,2),A,b)
print(v)