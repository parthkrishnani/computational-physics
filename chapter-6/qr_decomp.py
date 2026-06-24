from numpy import *
from scipy import linalg
A=array([[1,4,8,4],
         [4,2,3,7],
         [8,3,6,9],
         [4,7,9,2]],float)
N,c=shape(A)
V=eye(N)
U=zeros([N,N])
Q=zeros([N,N])

for i in range(N):
    U[:,i]=A[:,i]
    
    for j in range(i):
        U[:,i]-=dot(Q[:,j],A[:,i])*Q[:,j]
    
    Q[:,i]=U[:,i]/linalg.norm(U[:,i])
R = Q.T @ A
print("Q=", Q)
print("R=", R)