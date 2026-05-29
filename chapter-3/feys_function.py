import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,24*np.pi,1000)
r=np.e**(np.cos(theta))-2*np.cos(4*theta)+np.sin(theta/12)**5
plt.polar(theta,r)
plt.grid(True)
plt.show()