from vpython import *
import numpy as np
s=np.empty(7, sphere)
c1=2.5*10**3
c2=0.01
x=1000
s[0]=sphere(pos=vector(x+57.9,0.0,0.0),radius=c1*0.00244, color=color.green)
s[1]=sphere(pos=vector(x+108.2,0.0,0.0),radius=c1*0.006052, color=color.cyan)
s[2]=sphere(pos=vector(x+149.6,0.0,0.0),radius=c1*0.006371, color=color.blue)
s[3]=sphere(pos=vector(x+227.9,0.0,0.0),radius=c1*0.003386, color=color.red)
s[4]=sphere(pos=vector(x+778.5,0.0,0.0),radius=c1*0.069173, color=color.magenta)
s[5]=sphere(pos=vector(x+1433.4,0.0,0.0),radius=c1*0.057316, color=color.orange)
s[6]=sphere(pos=vector(0.0,0.0,0.0),radius=695.5, color=color.yellow)
theta=np.zeros(7)
while True:
    rate(100000)
    s[0].pos.x = (x+57.9)*np.cos(theta[0])
    s[0].pos.y = (x+57.9)*np.sin(theta[0])
    theta[0] += c2/88 
    s[1].pos.x = (x+108.2)*np.cos(theta[1])
    s[1].pos.y = (x+108.2)*np.sin(theta[1])
    theta[1] += c2/224.7
    s[2].pos.x = (x+149.6)*np.cos(theta[2])
    s[2].pos.y = (x+149.6)*np.sin(theta[2])
    theta[2] += c2/365.3
    s[3].pos.x = (x+227.9)*np.cos(theta[3])
    s[3].pos.y = (x+227.9)*np.sin(theta[3])
    theta[3] += c2/687 
    s[4].pos.x = (x+778.5)*np.cos(theta[4])
    s[4].pos.y = (x+778.5)*np.sin(theta[4])
    theta[4] += c2/4331.6
    s[5].pos.x = (x+1433.4)*np.cos(theta[5])
    s[5].pos.y = (x+1433.4)*np.sin(theta[5])
    theta[5] += c2/10759.2
