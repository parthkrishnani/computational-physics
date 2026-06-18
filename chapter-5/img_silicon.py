import matplotlib.pyplot as plt
import numpy as np

h=2.5
w=np.loadtxt('chapter-5/stm.txt')
row,col=np.shape(w)
dwx = np.zeros((row, col))
for j in range(col):
    for i in range(row):
        if i == row - 1:
            dwx[i,j] = (w[i,j] - w[i-1,j]) / h
        else:
            dwx[i,j] = (w[i+1,j] - w[i,j]) / h

dwy = np.zeros((row, col))
for i in range(row):
    for j in range(col):
        if j == col - 1:
            dwy[i,j] = (w[i,j] - w[i,j-1]) / h
        else:
            dwy[i,j] = (w[i,j+1] - w[i,j]) / h

p=5*np.pi/4
I=-(np.cos(p)*dwx+np.sin(p)*dwy)/np.sqrt(dwx**2+dwy**2+1)

plt.imshow(I,cmap='gray',origin='upper')
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.title("Silicon Surface Map")
plt.show()