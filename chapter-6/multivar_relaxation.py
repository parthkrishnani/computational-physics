from numpy import *

a = 1
b = 2

def f(x, y):
    return x / (a + x**2)

def g(x, y):
    return sqrt(b/y - a)

def d(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

x_ = 0.5
y_ = 0.5
w = 0.5
err = 1
itr = 0

while err > 1e-6:
    x1 = (1 - w) * x_ + w * g(x_, y_)
    y1 = (1 - w) * y_ + w * f(x_, y_)

    dg = d(lambda x: g(x, y_), x_)
    df = d(lambda y: f(x_, y), y_)

    denom_x = 1 - (1 / ((1 + w) * dg - w))
    denom_y = 1 - (1 / ((1 + w) * df - w))

    err_x = abs((x_ - x1) / denom_x)
    err_y = abs((y_ - y1) / denom_y)
    err = sqrt(err_x**2 + err_y**2)

    x_ = x1
    y_ = y1
    itr += 1

print(f"Solution: x = {x_:.6f}, y = {y_:.6f}")
print(f"Iterations: {itr}")