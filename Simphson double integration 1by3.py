# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:45:29 2022

@author: Rifa Tabassum Mim
lab: Simphson's double integration'
"""

import numpy as np

def fun(x,y):
    f_xy = 1/(x*y)
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
for i in range(n+1):
    for j in range(n+1):
        f_XY[i][j] = fun(X[i],Y[j])
        #print( f_XY[i][j])
        
#For integrating in X axis
I=np.zeros([n+1])
for i in range(n+1):
    for j in range(n+1):
        if j==0:
            I[i] = I[i]+((h1/3)*f_XY[j][i])
        #print(I)
        if j>0 and j%2!=0:
            I[i] = I[i]+(h1*(4/3)*f_XY[j][i])
        if j%2 == 0 and j>0:
            I[i] = I[i]+(h1*(2/3)*f_XY[j][i])
    print(I[i])  

#Finding Integration in y axis
I_y = 0
for k in range(n+1):
    if k == 0:
        I_y = I_y+((h2/3)*I[i])
    if k%2 == 0 and k>0:
        I_y = I_y+ (h2*(2/3)*I[i])
    if k%2 != 0 and k>0:
        I_y = I_y + (h2*(4/3)*I[i])
print(f'The value of integration: {I_y}')
