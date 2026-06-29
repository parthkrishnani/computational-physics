from numpy import *
import matplotlib.pyplot as plt

def p(x):
    return 924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1
def dp(x):
    return 6*924*x**5-5*2772*x**4+4*3150*x**3-3*1680*x**2+2*420*x-42

err=1e-10
delta=1
roots = []
for x0 in [0.05, 0.2, 0.35, 0.5, 0.65, 0.85]:
    x = x0
    delta = 1
    while abs(delta) > err:
        dp_val = dp(x)
        if abs(dp_val) < 1e-14:
            x += 1e-6
            continue
        delta = p(x) / dp_val
        x -= delta
    roots.append(x)

print(roots)