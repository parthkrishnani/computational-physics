import vpython as vp
import numpy as np
L=5
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if (i+j+k)%2==0:
                vp.sphere(pos=vp.vector(i,j,k), radius=0.3, color=vp.color.red)
            else:
                vp.sphere(pos=vp.vector(i,j,k), radius=0.3, color=vp.color.white)