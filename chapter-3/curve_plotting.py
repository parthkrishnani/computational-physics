import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,2*np.pi,100)
x=2*np.cos(theta)+np.cos(2*theta)
y=2*np.sin(theta)-np.sin(2*theta)
r=np.sqrt(x**2+y**2)
plt.polar(theta,r)
plt.grid(True)
plt.show()