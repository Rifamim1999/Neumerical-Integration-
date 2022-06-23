# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:49:51 2022

@author: Rifa Tabasssum Mim
Lab: Trapezoidal Rule
"""
import numpy as np
import math
#creating a function 
def f(x):
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
    f_x[i] = f(X[i])
    #print(f_x[i])

I = 0
for i in range(n+1):
    if i==0:
        I = I+((h/2)*f_x[i])
        #print(I)
    if i>0 and i!=n:
        I = I+(h*f_x[i])
    if i == n:
        I = I+((h/2)*f_x[i])
print(f'The integration: {I}')



