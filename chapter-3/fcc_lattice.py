import vpython as vp
import numpy as np
a=1
for i in range(-a, a+1):
    for j in range(-a, a+1):
        for k in range(-a, a+1):
            if i==j==k==0:
                continue
            else:
                vp.sphere(pos=vp.vector(i,j,k), radius=0.3, color=vp.color.red)

                