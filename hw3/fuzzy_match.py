# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:18:27 2014

@author: anneubuntu
"""

#def search_genome_lev(genome,query,threshold):
    
def fuzzy_match(s1,s2):
    if len(s1) ==0:
        return len(s2)
    if len(s2)==0:
        return len(s1)
    case1 = fuzzy_match(s1[1:],s2) + 1
    case2 = fuzzy_match(s1,s2[1:]) + 1
    if s1[0]!=s2[0]:
        case3 = 1 + fuzzy_match(s1[1:],s2[1:])
    else:
        case3 = fuzzy_match(s1[1:],s2[1:])
    return min([case1,case2,case3])
    
if __name__ == "__main__":
    print fuzzy_match("urppe","purpe")