# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:43:15 2014

@author: anneubuntu
"""

x = int(raw_input("Enter x: "))
y = int(raw_input("Enter y: "))

print comparexy(x,y)

def comparexy(x,y):
    if(x>y):
        return 1
    elif(y>x):
        return -1
    else:
        return 0
        

        