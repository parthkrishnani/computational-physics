import matplotlib.pyplot as plt
import numpy as np
data=np.loadtxt('chapter-3/circular.txt')
plt.imshow(data,origin='lower')
plt.colorbar()
plt.title('Heat Map')
plt.show()