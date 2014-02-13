# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:56:36 2014

@author: anneubuntu
"""

def get_complementary_base(a):

        if(a=='A'):
            return "T"
        elif(a=="T"):
            return "A"
        elif(a=="G"):
            return "C"
        elif(a=="C"):
            return "G"
        else:
            print "Error: not a nucleotide"
            return None
    