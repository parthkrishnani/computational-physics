import numpy as np
a=0.001
b=1000
c=0.001
x1=2*c/(-b-np.sqrt(b**2-4*a*c))
x2=(-b-np.sqrt(b**2-4*a*c))/(2*a)
print(x1)
print(x2)