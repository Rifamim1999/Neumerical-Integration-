# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:11:48 2022

@author: Rifa Tabassum Mim
lab: Double integration Trapezoidal
"""

import numpy as np

def f(x,y):
    f_xy = (2*x*y) + (2*x) - (pow(x,2)) - (pow(y,2)*2) + 72
    return f_xy

x0 = float(input("Enter the first vallue of x: "))
xn = float(input("Enter the last vallue of x: "))
y0 = float(input("Enter the first vallue of y: "))
yn = float(input("Enter the last vallue of y: "))
n = int(input("Enter the number of segments: "))

#width of each x segment
h1 = (xn-x0)/n
#width of each y segment
h2 = (yn-y0)/n

#values of y
Y = np.zeros([n+1])
X = np.zeros([n+1])

#finding all x and y 
for i in range(n+1):
    Y[i] = y0+(i*h2)
    X[i] = x0+(i*h1)
    
#creating an array to store the functional values
f_XY = np.zeros([n+1 , n+1])
I=np.zeros([n+1])
for i in range(n+1):
    for j in range(n+1):
        f_XY[i][j] = f(X[i],Y[j])
        #print( f_XY[i][j])
#For integrating in X axis
for i in range(n+1):
    for j in range(n+1):
        if j==0:
            I[i] = I[i]+((h1/2)*f_XY[j][i])
        #print(I)
        if j>0 and j!=n:
            I[i] = I[i]+(h1*f_XY[j][i])
        if j == n:
            I[i] = I[i]+((h1/2)*f_XY[j][i])
    print(I[i])  
#reversed(I)
#For Integrating in Y axis
I_Y = 0
for k in range(n+1):
    if k == 0:
        I_Y = I_Y + ((h2/2)*I[k])
    if k>0 and k != n:
        I_Y = I_Y + (h2*I[k])
    if k == n:
        I_Y = I_Y + ((h2/2)*I[k])
print(f"The Integration of given Function: {I_Y}")
        

