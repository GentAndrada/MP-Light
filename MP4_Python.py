# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:00:22 2019

@author: Samsung
"""
import numpy as np
import matplotlib.pyplot as plt 
import math
h = float(input('Type the initial height in meters: '));
v = float(input('Magnitude of the velocity in m/s: '));
theta = float(input('Angle in degrees: '));
ax = float(input('X-component of the acceleration: '));
ay = float(input('Y-component of the acceleration: '));

class Error(Exception):
   """Base class for other exceptions"""
   pass
class ayCannotBeZeroError(Error):
   """Raised when the input value of ay is zero"""
   pass

thetarad = math.radians(theta)
while True:
 try: 
  for t in range(0,1000,1):
     x = v*math.cos(thetarad)*t + (ax*(t)**2)/2;
     
     y = v*math.sin(thetarad)*t + (ay*(t)**2)/2 + h;
    
 except ayCannotBeZeroError:
     print('The input value of ay cannot be zero')
     print()
     
x1 = np.array(x)
y1 = np.array(y)
tmax = (v*math.sin(thetarad))/(-ay);
ymax = v*math.sin(thetarad)*tmax + (ay*(tmax)**2)/2;
total = ymax + h + 10;
plt.plot(x,y)
plt.ylim((0,total));
plt.xlabel('x - coordinate') 
plt.ylabel('y - coordinate')
plt.title('Projectile Motion')
plt.show()
  