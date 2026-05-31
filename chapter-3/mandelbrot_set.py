import matplotlib.pyplot as plt
import numpy as np
N=1000
x_values=np.linspace(-2,2,N)
y_values=np.linspace(-2,2,N)
c=0
z=0
z_plot=[]
c_plot=[]
for x in x_values:
    for y in y_values:
        c=x+y*1j
        z=0
        for i in range(100):
            z=z**2+c
            if abs(z)>2:
                break
        for i in range(2*N-1):
            z=z**2+c
            if abs(z)>2:
                break
            else:
                z_plot.append(z)
                c_plot.append(c)
plt.plot([c.real for c in c_plot], [c.imag for c in c_plot], '.', markersize=0.5)
plt.grid(True)
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Mandelbrot Set')
plt.show()