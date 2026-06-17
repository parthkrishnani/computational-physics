import matplotlib.pyplot as plt
import numpy as np

def v(x, y, q):
    eps = 8.854e-12
    r = np.sqrt(x**2 + y**2)
    r = np.where(r == 0, 1e-9, r)   
    return q / (4 * np.pi * eps * r)
h=10**(-6)
def del_op(u,x,y):
    E_x=-(u(x+h,y)-u(x,y))/h
    E_y=-(u(x,y+h)-u(x,y))/h
    return [E_x,E_y]
x=np.linspace(-10, 10, 1000)
y=np.linspace(-10,10, 1000)
XX, YY = np.meshgrid(x,y)
q = -10
potential = v(XX, YY, q)
u = lambda x, y: v(x, y, q)

Ex, Ey = del_op(u, XX, YY)
E_mag = np.sqrt(Ex**2 + Ey**2)


plt.imshow(potential, extent=[-10, 10, -10, 10], origin='lower', cmap='RdBu')
plt.colorbar(label='V (volts)')
plt.title('Electric potential')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()

plt.imshow(E_mag, extent=[-10, 10, -10, 10], origin='lower',
           cmap='hot', vmax=np.percentile(E_mag, 99))
plt.title('Electric Field (Magnitude)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()