import numpy as np
def f(x):
    return x*(x-1)
def df(x):
    d=10**-10
    return (f(x+d)-f(x))/(d)
print(df(1))