import numpy as np
from gaussxw import gaussxwab
import matplotlib.pyplot as plt
L=5
M=10*10**3
G=6.674*10**(-11)
sig=M/(L**2)
N=100
x_pt, x_wt = gaussxwab(N, -L/2, L/2)
y_pt, y_wt = gaussxwab(N, -L/2, L/2)
XX, YY = np.meshgrid(x_pt, y_pt) #Improvement over using a triple nested loop
WW = np.outer(x_wt, y_wt) #Calculates the weight of each point on the grid
z = np.linspace(0,10,1000)
g=np.zeros(len(z))
for i in range(0,len(z)-1):
    d=np.sqrt(XX**2+YY**2+z[i]**2)
    g[i]=G*sig*z[i]*np.sum(WW/d**3)
plt.plot(z,g)
plt.xlabel('z')
plt.ylabel('Fz')
plt.grid()
plt.show()