import numpy as np
from gaussxw import gaussxwab
import matplotlib.pyplot as plt
def V(x):
    return x**4
a_lin=np.linspace(0,2,100)
V_lin=V(a_lin)
T_lin=np.zeros(len(a_lin))
N=20
kp=0
for a in a_lin:
    E=V(a)
    x,w=gaussxwab(N,0,a)
    S=0
    for k in range(N):
        S+=w[k]/np.sqrt(E-V(x[k]))
    T=2*S
    T_lin[kp]=T
    kp+=1
plt.plot(a_lin,T_lin)
plt.xlabel('Amplitude (a)')
plt.ylabel('Period (T)')
plt.title('Period of Anharmonic Oscillator')
plt.grid()
plt.show()