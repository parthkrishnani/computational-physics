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

x=np.linalg.solve(A,b)
print(x)