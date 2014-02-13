# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Anne LoVerso
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from load import load_seq, load_salmonella_genome
from random import shuffle



def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    pros = ""
    l = len(dna)
    for i in range(0,l,3):
        code = dna[i:i+3]
        for j in range(len(codons)):
            a = codons[j]
            if code in a:
                p = aa[j]
                pros = pros + p
    return pros
        

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    print coding_strand_to_AA("ATGCGA")
    print "Expected: MR"
    print coding_strand_to_AA("GCTAATAACGAA")
    print "Expected: ANNE"

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    from get_complementary_base import get_complementary_base
    back = ""
    l = len(dna)
    for i in range(l):
        bit = dna[i:i+1]
        bitnew = get_complementary_base(bit)
        back = bitnew + back
    return back
    
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print get_reverse_complement("AATG")
    print "Expected: CATT"
    print get_reverse_complement("ATGATGATG")
    print "Expected: CATCATCAT"
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    stop_codons = ["TAG","TAA","TGA"]
    rest=dna
    l = len(dna)
    for i in range(0,l,3):
        code = dna[i:i+3]
        if code in stop_codons:
            rest = dna[:i]
            return rest
    return dna
        

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    print rest_of_ORF("ATGACGTACGCACGATAA")
    print "Expected: ATGACGTACGCACGA"
    print rest_of_ORF("ATGATCATCATTAG")
    print "Expected: ATGCATCATCAT"
    print rest_of_ORF("ATGAGTAC")
    print "Expected: ATGAGTAC"
    

        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    start = "ATG"
    index=0
    all_orfs = []
    l = len(dna)
    while(index<l):
        if dna[index:index+3]==start:
            rest = rest_of_ORF(dna[index:])
            all_orfs.append(rest)
            index = index + len(rest)
        else:
            index = index + 3
    return all_orfs
            
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    print find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    print "Expected: ATGCATGAATGTAGA, ATGTGCCC"

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    all_orfs = []
    for i in range(3):
        new_dna = dna[i:]
        all_orfs += (find_all_ORFs_oneframe(new_dna))
    return all_orfs

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print find_all_ORFs("ATGCATGAATGTAG")
    print "ATGCATGAATGTAG, ATGAATGTAG, ATG"
    

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    alls = []
    alls += find_all_ORFs(dna)
    alls += find_all_ORFs(get_reverse_complement(dna))
    return alls    
    
def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    print "ATGCGAATG, ATGCTACATTCGCAT"
    
def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    orfs = find_all_ORFs_both_strands(dna)
    longest = orfs[0]
    for x in orfs:
        if len(x) > len(longest):
            longest = x
    return longest

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    print longest_ORF("ATGCGAATGTAGCATCAAA")
    print "ATGCTACATTCGCAT"
    
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    dna_array = list(dna)
    longest = ""
    for i in range(num_trials):
        shuffle(dna_array)
        dna_string = collapse(dna_array)
        orf = longest_ORF(dna_string)
        if len(orf) > len(longest):
            longest = orf
    return len(longest)
    

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    orfs = find_all_ORFs_both_strands(dna)
    good_orfs = []
    amino_seq = []
    for x in orfs:
        if len(x) > threshold:
            good_orfs.append(x)
    for x in good_orfs:
        amino_seq.append(coding_strand_to_AA(x))
    return amino_seq
    
"""    
Next, use your longest_ORF_noncoding on the Salmonella DNA sequence and compute a 
conservative threshold for distinguishing between genes and non-genes by running 
longest_ORF_noncoding for 1500 trials.  Make a note of this number as it will be 
used with the gene_finder function.

Next, use your gene_finder function with the original Salmonella DNA sequence 
and the threshold computed above to get a list of candidate genes.

Finally, take the amino acid sequences produced by your gene finder and search
 for them using protein-BLAST.  What types of genes appear to be in this DNA 
 sequence?  Record your findings in a file called salmonella.txt.
"""

if __name__ == "__main__":
    dna = load_seq("./data/X73525.fa")
    #threshold = 5000
    threshold = longest_ORF_noncoding(dna,1500)
    sequence = gene_finder(dna,threshold)
    print sequence




"""
How to debug:
Spyder debugging tool
r command to run
use breakpoints
p to print at some point
"""


