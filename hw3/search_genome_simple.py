# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:53:07 2014

@author: anneubuntu
"""

def search_genome_simple(genome,query):
    protein_names = []
    for x in genome:
       if len(x)==3: 
           if query in x[2]:
              protein_names.append(x[1])
    return protein_names
