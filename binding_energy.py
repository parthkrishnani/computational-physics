import numpy as np
#The values of all the following constants required to compute binding energy are in terms of MeV
a1=15.8
a2=18.3
a3=0.714
a4=23.2
bmin=0
for Z in range(1, 101):
    for A in range(int(Z), int(3*Z)+1):
        B=a1*A - a2*(A**(2/3)) - a3*(Z**2/A**(1/3)) - a4*(((A-2*Z)**2)/A)
        b = B/A
        if b > bmin:
            bmin = b
            Amax = A
            Zmax = Z
print("The maximum binding energy per nucleon is", bmin, "MeV at A =", Amax, "and Z =", Zmax)