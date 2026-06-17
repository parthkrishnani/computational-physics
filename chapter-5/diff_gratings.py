import numpy as np
from gaussxw import gaussxwab
import matplotlib.pyplot as plt
a=20*10**(-6)
wv=500*10**(-9)
f=1
def q(u):
    return (np.sin(a*u))**2
u,w=gaussxwab(100,-0.05,0.05)
def I(x,y):
    integrand=np.sqrt(q(u))*np.exp((2*np.pi*(x*u)*1j)/(wv*f))
    return abs(np.dot(w, integrand))
N = 500
x_vals = np.linspace(-0.01, 0.01, N)
y_vals = np.linspace(-0.01, 0.01, N)

I_grid = np.array([[I(x, y) for x in x_vals] for y in y_vals])

plt.imshow(I_grid, extent=[-0.01, 0.01, -0.01, 0.01], origin='lower')
plt.colorbar(label='Intensity')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Grating Diffraction Pattern')
plt.show()