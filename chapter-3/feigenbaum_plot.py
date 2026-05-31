import matplotlib.pyplot as plt
import numpy as np
x_plot=[]
r_values=np.linspace(1,4,300)
r_plot=[]
for r in r_values:
    x=0.5
    for i in range(1000):
        x=r*x*(1-x)
    for i in range(1000):
        x=r*x*(1-x)
        x_plot.append(x)
        r_plot.append(r)
print(r_plot)
plt.plot(r_plot,x_plot,'.',markersize=0.5)
plt.xlabel('r')
plt.ylabel('x')
plt.title('Feigenbaum Plot')
plt.show()