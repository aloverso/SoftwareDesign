# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:30:00 2014

@author: anneubuntu
"""

def makeGrid():
    horiz1 = "+ - - - - + - - - - +"
    horiz2 = "|         |         |"
    print horiz1
    for i in range(0,2):
        for j in range(0,4):
            print horiz2
        print horiz1

makeGrid()