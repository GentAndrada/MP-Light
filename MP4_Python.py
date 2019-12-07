# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 01:19:07 2019

@author: Samsung
"""

import numpy as np
import matplotlib.pyplot as plt 
import math
h = float(input('Type the initial height in meters: '));
v = float(input('Magnitude of the velocity in m/s: '));
theta = float(input('Angle in degrees: '));
ax = float(input('X-component of the acceleration in m/s^2: '));
ay = float(input('Y-component of the acceleration in m/s^2: '));
thetarad = math.radians(theta)

tflight = (2*(v*math.sin(thetarad)+h))/-ay;
t = np.linspace(0,float(tflight),60);

def x(t):
    return v*np.cos(thetarad)*t + (ax*(t)**2)/2;

def y(t):
    return v*np.sin(thetarad)*t + (ay*(t)**2)/2 + h;

tmax = (v*math.sin(thetarad))/(-ay);
ymax = v*math.sin(thetarad)*tmax + (ay*(tmax)**2)/2;
total = ymax + h + 10;

plt.plot(x(t),y(t))
plt.grid()
plt.ylim(0,total)
plt.xlabel('x - coordinate') 
plt.ylabel('y - coordinate') 
plt.title('Projectile Motion') 
plt.show()