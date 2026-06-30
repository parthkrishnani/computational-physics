from numpy import *
import matplotlib.pyplot as plt

G=6.674e-11
M=5.794e24
m=7.348e22
R=3.844e8
omega=2.662e-6

def L(r):
    return G*M/r**2 - G*m/(R-r)**2 - omega**2*r

err=1
x1=3.2e8
x2=3.19e8

while err>1e-4:
    x2_=x2-L(x2)*(x2-x1)/(L(x2)-L(x1))
    x1=x2
    err=abs(x2-x2_)
    x2=x2_

print(x2)