import matplotlib.pyplot as plt
import numpy as np
data=np.loadtxt('chapter-3/sunspots.txt')
x=data[:1000,0]
y=data[:1000,1]
Yk=[]
for k in range(0,1000):
    xk=0
    for m in range(-5,6):
        if k+m>=0 and k+m<1000:
            b=k+m
            xk+=y[b]
        else:
            continue
    Yk.append(xk/11)
plt.plot(x,y,color='blue')
plt.plot(x,Yk,color='red')
plt.xlabel('Year')
plt.ylabel('Number of Sunspots')
plt.title('Sunspot Data')
plt.show()