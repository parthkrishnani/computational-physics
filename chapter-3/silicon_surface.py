import matplotlib.pyplot as plt
import numpy as np
data=np.loadtxt('chapter-3/stm.txt')
plt.imshow(data,origin='lower')
plt.show()