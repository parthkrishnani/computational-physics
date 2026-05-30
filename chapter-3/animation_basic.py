import vpython as vp
import numpy as np
s=vp.sphere(pos=vp.vector(10,0,0), radius=0.5, color=vp.color.white)
theta = 0

while True:
    vp.rate(60)
    s.pos.x = 10*np.cos(theta)
    s.pos.y = 10*np.sin(theta)
    theta += 0.05