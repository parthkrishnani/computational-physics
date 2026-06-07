import numpy as np
n=np.zeros(13)
for i in range(13):
    n[i]=2**(i)
def f(x):
    return (np.sin(10*np.sqrt(x)))**2
a=0
b=2
I=np.zeros(13)
h=np.zeros(13)
for i in range(13):
    h[i]=(b-a)/n[i]
err=np.zeros(13)
I[0] = h[0] * (0.5*f(a) + 0.5*f(b))
print('n=1, Integral=',I[0])
for i in range(1,13):
    I[i]=0.5*I[i-1]
    for j in range(1,int(n[i]),2):
        I[i]+=f(a+j*h[i])
    I[i]*=h[i]
    print('n=',int(n[i]),', Integral=',I[i])
for i in range(1,13):
    err[i]=abs(I[i]-I[i-1])/3
    print('n=',int(n[i]),', Error estimate=',err[i])

