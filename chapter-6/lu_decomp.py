import numpy as np
A=np.array([[0,1,4,1],
            [3,4,-1,-1],
            [1,-4,1,5],
            [2,-2,1,3]],float)
b=np.array([-4,3,9,7],float)
N=len(b)
for m in range(N):
    if A[m,m]==0:
        if m<N-1:
            A[[m, m+1]] = A[[m+1, m]]
            b[[m,m+1]] = b[[m+1,m]]
        else:
            A[[m, m-1]] = A[[m-1, m]]
            b[[m,m-1]] = b[[m-1,m]]
U=A.copy()
L=np.zeros([N,N])
for i in range(N):
    div = U[i,i]
    U[i,:]/=div
    b[i]/=div
    for j in range(i+1,N):
        mul=U[j,i]
        L[j,i]=mul
        U[j,:]-=mul*U[i,:]
        b[j]-=mul*b[i]
print("U=",U)
print("L=",L)