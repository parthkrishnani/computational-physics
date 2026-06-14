import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.tanh(x)
x_lin=np.linspace(-10,10,2000)
f_lin=np.zeros(len(x_lin))
for i in range(len(x_lin)):
    f_lin[i]=f(x_lin[i])
der_lin=np.zeros(len(x_lin))
h=10**(-5)
def deri(x):
    return (f(x+(h/2))-f(x-(h/2)))/h
for i in range(len(x_lin)):
    der_lin[i]=deri(x_lin[i])
plt.plot(x_lin, f_lin)
plt.plot(x_lin, der_lin)
plt.grid()
plt.xlabel("x")
plt.ylabel("F, dF")
plt.title("Plot of hyperbolic tan and its derivative")
plt.show()