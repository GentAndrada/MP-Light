# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:38:01 2019

@author: Samsung
"""

import math
import matplotlib.pyplot as plt 
xvalue = []
yvalue = []
for n in range(0,200):
    x = math.sin((3*math.pi*n)/100)
    xvalue.append(x)
    
for n in range(0,200):
    if n==0:
        y = -1.5*xvalue[n]+2*xvalue[n+1] - 0.5*xvalue[n+2];
    elif n>0 and n<198:
        y =  0.5*xvalue[n+1]-0.5*xvalue[n-1];
    elif n==199:
        y =  1.5*xvalue[n]-2*xvalue[n-1]+0.5*xvalue[n-2];
    else:
        y = None;
    yvalue.append(y)


plt.plot(xvalue, label = 'x(n)')
plt.plot(yvalue, label = 'y(n)')
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.legend()
plt.title('Machine Problem 5') 
plt.show()
