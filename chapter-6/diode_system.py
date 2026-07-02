import numpy as np
V_p=5
R1=1e3
R2=4e3
R3=3e3
R4=2e3
I0=3e-9
VT=0.05
H_=1e-5

def f(x1,x2):
    return (x1/R2)+((x1-V_p)/R1)+(I0*(np.exp((x1-x2)/VT)-1))
def g(y1,y2):
    return (y2/R4)+((y2-V_p)/R3)+(I0*(np.exp((y2-y1)/VT)-1))
def d1(n,u,v):
    return (n(u+H_,v)-n(u,v))/H_
def d2(N,U,V):
    return (N(U,V+H_)-N(U,V))/H_

err = 1
x1, x2 = 1.0, 1.0  

while err > 1e-10:
    J = np.array([[d1(f, x1, x2), d2(f, x1, x2)],
                  [d1(g, x1, x2), d2(g, x1, x2)]])
    
    F = np.array([f(x1, x2), g(x1, x2)])
    
    dx = np.linalg.solve(J, -F)
    
    x1 += dx[0]
    x2 += dx[1]
    
    err = np.sqrt(dx[0]**2 + dx[1]**2)

print(f"V1 = {x1:.6f} V")
print(f"V2 = {x2:.6f} V")