# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:06:49 2022

@author: Rifa Tabassum Mim
Topic: Gauss Jordan
"""
import numpy as np
import xlwt
import pandas as pd
import math

data = pd.read_excel("data_for_jordan.xlsx")
print(data)
r1 = data.iloc[0] 
row1 = np.zeros([len(r1)])
for i in range(len(r1)):
    row1[i] = r1[i]
print(row1)
r2 = (data.iloc[1]- (data.iloc[0] *(data.iloc[1,0]/data.iloc[0,0])))
row2 = np.zeros([len(r2)])
for i in range(len(r2)):
    row2[i] = r2[i]
#roww2 = row2/row2[1]   
print(row2)  

r3 = data.iloc[2]-(data.iloc[0]*(data.iloc[2,0]/data.iloc[0,0]))
r4 = r3-(row2*(r3[1]/row2[1]))
#print(r4)
#r5 = r4/r4[2]
#print(r5)
row3 = np.zeros([len(r4)])
for i in range(len(r4)):
    row3[i] = r4[i]
print(row3)

r6 = row2 - ((row1*row2[1])/row1[1])
print(r6)
r7 = row3-((r6*row3[2])/r6[2])
print(r7)  #row1 of identical matrix
r8 = row3 - ((row2*row3[2])/row2[2])
print(r8)
x1 = r7[3]/r7[0]
x2 = r8[3]/r8[1]
x3 = row3[3]/row3[2]
print("x1: {}".format(x1))
print("x2: {}".format(x2))
print("x3: {}". format(x3))
 
