import vpython as vp
from numpy import empty,zeros,array,exp,cos,pi
from scipy import linalg as la
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k-m*omega*omega

A = empty([3,N],float)
for i in range(N):
    A[0,i] = -k
    A[1,i] = alpha
    A[2,i] = -k
A[1,0] = alpha - k
A[1,N-1] = alpha - k

v = zeros(N,float)
v[0] = C

x = la.solve_banded((1,1), A, v) 
particles = []

for i in range(-N//2, N//2):
    particles.append(
        vp.sphere(
            pos=vp.vector(i*2,0,0),
            radius=0.3
        )
    )

dt = 0.01

scale = 20
phase=0
while True:
    vp.rate(100)
    phase = (phase + omega*dt) % (2*pi)
    for i in range(N):
        particles[i].pos.x = ((i-N//2)*2+ scale*x[i]*cos(phase))

