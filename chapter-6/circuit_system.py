import numpy as np
A=np.array([[4,1,1,1],
            [-1,-1,-1,3],
            [-1,0,-1,3],
            [-1,3,0,-1]],float)
v_pl=5
v=np.array([v_pl,0,v_pl,0],float)
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