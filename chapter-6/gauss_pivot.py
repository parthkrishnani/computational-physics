import numpy as np
A=np.array([[0,1,4,1],
            [3,4,-1,-1],
            [1,-4,1,5],
            [2,-2,1,3]],float)
r,c=np.shape(A)
b=np.array([-4,3,9,7],float)
for m in range(r):
    if A[m,m]==0:
        if m<r-1:
            A[[m, m+1]] = A[[m+1, m]]
            b[[m,m+1]] = b[[m+1,m]]
        else:
            A[[m, m-1]] = A[[m-1, m]]
            b[[m,m-1]] = b[[m-1,m]]
x=np.empty(r)
for k in range(r):
    d=A[k,k]
    A[k,:]/=d
    b[k]/=d
    for j in range(k+1,r):
        mul=A[j,k]
        A[j,:]-=mul*A[k,:]
        b[j]-=mul*b[k]
for i in range(r-1,-1,-1):
    x[i]=b[i]
    for l in range(i+1,r):
        x[i]-=A[i,l]*x[l]
print(x)