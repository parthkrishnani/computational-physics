import matplotlib.pyplot as plt
from numpy import *

V=20
w=1
hbar=6.582e-16
m=1

def y1(x):
    return tan(sqrt(w**2*m*x/(2*hbar**2)))
def y2(x):
    return sqrt((V-x)/x)
def y3(x):
    return -sqrt(x/(V-x))

E=linspace(0,20,20000)
Y1=y1(E)
Y2=y2(E)
Y3=y3(E)

Y1_masked = ma.masked_where(abs(Y1) > 50, Y1)

plt.plot(E, Y1_masked, label=r'$\tan(\sqrt{mE/2\hbar^2}\cdot w)$')
plt.plot(E, Y2, label=r'$\sqrt{(V-E)/E}$')
plt.plot(E, Y3, label=r'$-\sqrt{E/(V-E)}$')

plt.ylim(-10, 10)
plt.xlabel("E")
plt.ylabel("Y(E)")
plt.legend()
plt.grid()
plt.show()