import numpy as np
def f(x):
    return np.sin(10*np.sqrt(x))
a=0 #lower limit
b=2 #upper limit
M=5
R_vals=np.zeros([M,M]) #Romberg triangle values
I_vals=np.zeros(M) #Trapezoidal integration values
N=np.zeros(M)
for i in range(M):
    N[i]=2**i
h=np.zeros(M)
for i in range(M):
    h[i]=(b-a)/N[i]
I_vals[0]=0.5*h[0]*(f(b)-f(a)) #defining first integral using Traperzoidal rule
for i in range(1,M):
    I_vals[i]=0.5*I_vals[i-1]
    for j in range(1,int(N[i]),2):
        I_vals[i]+=f(a+j*h[i])
    I_vals[i]*=h[i]

for i in range(M):
    R_vals[i,0]=I_vals[i]

for i in range(1,M):
    for j in range(i):
        R_vals[i,j+1]=R_vals[i,j]+(R_vals[i,j]-R_vals[i-1,j])/((4**i)-1)
print(R_vals)