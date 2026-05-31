import numpy as np
kBT=100
beta=1/kBT
Z=0
S=0
for n in range(1000000):
    E=n+0.5
    Z+=np.exp(-beta*E)
    S+=E*np.exp(-beta*E)
S=S/Z
print(S)