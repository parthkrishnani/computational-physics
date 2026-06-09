from gaussxw import gaussxw
import numpy as np
def f(x):
    return x**4-2*x+1
a=0 #lower limit
b=2 #upper limit
N=10
x,w=gaussxw(N)
xp=0.5*(b-a)*x+0.5*(b+a)
wp=0.5*(b-a)*w
s=0
for k in range(N):
    s+=wp[k]*f(xp[k])
print(s)