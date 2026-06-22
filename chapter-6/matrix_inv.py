import numpy as np
A=np.array([[2,1,4,1],
            [3,4,-1,-1],
            [1,-4,1,5],
            [2,-2,1,3]],float)
r,c=np.shape(A)
I=np.eye(r)              
v1=I[0,:].copy()         
v2=I[1,:].copy()
v3=I[2,:].copy()
v4=I[3,:].copy()         

for m in range(r):
    d=A[m,m]
    A[m,:]/=d
    v1[m]/=d
    v2[m]/=d
    v3[m]/=d
    v4[m]/=d              
    for j in range(m+1,r):
        mul=A[j,m]
        A[j,:]-=mul*A[m,:]
        v1[j]-=mul*v1[m]
        v2[j]-=mul*v2[m]
        v3[j]-=mul*v3[m]
        v4[j]-=mul*v4[m]  

x1=np.empty(r,float)
x2=np.empty(r,float)
x3=np.empty(r,float)
x4=np.empty(r,float)
for i in range(r-1,-1,-1):   
    x1[i]=v1[i]
    x2[i]=v2[i]
    x3[i]=v3[i]
    x4[i]=v4[i]
    for k in range(i+1,r):   
        x1[i]-=A[i,k]*x1[k]
        x2[i]-=A[i,k]*x2[k]
        x3[i]-=A[i,k]*x3[k]
        x4[i]-=A[i,k]*x4[k]

A_inv=np.array([x1,x2,x3,x4]).T 
print(A_inv)