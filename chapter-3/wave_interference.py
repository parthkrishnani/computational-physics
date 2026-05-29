import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,1,100)
y=np.linspace(0,1,100)
X, Y = np.meshgrid(x, y)
xc=0.4
yc=0.5
xs=0.6
ys=0.5
r1=np.sqrt((X-xc)**2+(Y-yc)**2)
r2=np.sqrt((X-xs)**2+(Y-ys)**2)
del0=0.01
lambda_=0.05
k=2*np.pi/lambda_
def delta(r1,r2):
    delta_fin=del0*(np.sin(k*r1)+np.sin(k*r2))
    return delta_fin
delta_fin=delta(r1,r2)
plt.imshow(delta_fin,origin='lower')
plt.colorbar()
plt.title('Wave Interference Pattern')
plt.show()