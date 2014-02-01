# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:38:25 2014

@author: anneubuntu
"""

a = int(raw_input("Enter a: "))
b = int(raw_input("Enter b: "))
c = int(raw_input("Enter c: "))
n = int(raw_input("Enter n: "))


check_fermat(a,b,c,n)

def check_fermat(a,b,c,n):
    if(a**n + b**n == c**n and n>2):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."
        
