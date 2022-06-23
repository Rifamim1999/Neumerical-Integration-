# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:29:02 2022

@author: Rifa Tabassum Mim
lab: Simpson's 1/3 Rule'
"""

import numpy as np
import math
#creating a function 
def fun(x):
    fx = 0.2 + (25*x) - (pow(x, 2)*200) +(pow(x, 3)*675) -(pow(x, 4)*900) +(pow(x, 5)*400)
    return fx

#Taking the initial and last value
a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))
n = int(input("Enter the number of segments: "))  #taking the number of segments

#average width
h = (b-a)/n
print(f'The average width: {h}')
#creating an array for values of x
X = np.zeros([n+1])
for i in range(n+1):
    X[i] = a+(i*h)
    #print(X[i])

#creating a function array
f_x = np.zeros([n+1])
for i in range(n+1):
    f_x[i] = fun(X[i])
    #print(f_x[i])

#Finding Itegration
I=0
for i in range(n+1):
    if i == 0:
        I = I+((h/3)*f_x[i])
    if i%2 == 0 and i>0:
        I = I+ (h*(2/3)*f_x[i])
    if i%2 != 0 and i>0:
        I = I + (h*(4/3)*f_x[i])
print(f'The result of Integration is: {I}')
