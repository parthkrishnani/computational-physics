import numpy as np
A=np.array([[4,1,1,1],
            [-1,-1,-1,3],
            [-1,0,-1,3],
            [-1,3,0,-1]],float)
v_pl=5
b=np.array([v_pl,0,v_pl,0],float)
x=np.linalg.solve(A,b)
print(x)
