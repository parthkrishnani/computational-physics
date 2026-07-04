from numpy import *

sigma=1e-9
def V_V0(r):
    return (sigma/r)**6-exp(-r/sigma)

z=(sqrt(5)+1)/2

x1=sigma/10
x4=sigma*10
x2=x4-(x4-x1)/z
x3=x1+(x4-x1)/z

while (x4-x1)>1e-6:
    if V_V0(x2)<V_V0(x3):
        x4=x3
        x3=x2
        x2=x4-(x4-x1)/z
    else:
        x1=x2
        x2=x3
        x3=x1+(x4-x1)/z

print("The minimum falls at r = ",0.5*(x1+x4)*1e9,"nm")
