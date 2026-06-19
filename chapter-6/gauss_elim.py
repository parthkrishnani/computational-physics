import numpy as np
A=np.array([[2,1,4,1],
            [3,4,-1,-1],
            [1,-4,1,5],
            [2,-2,1,3]],float)
v=np.array([-4,3,9,7],float)
N=len(v)
for m in range(N):
    d=A[m,m]
    A[m,:]/=d
    v[m]/=d
    for j in range(m+1,N):
        mul=A[j,m]
        A[j,:]-=mul*A[m,:]
        v[j]-=mul*v[m]
x=np.empty(N,float)
for i in range(N-1,-1,-1):
    x[i]=v[i]
    for k in range(i+1,N):
        x[i]-=A[i,k]*x[k]
print(x)
