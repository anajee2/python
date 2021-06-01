# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"The first three bases are not ATG"
"The first three bases are not ATG"
"The last three bases are not a stop codon"
"The last three bases are not a stop codon"
"Sorry Can't Help You"




def orf_advisor(dna):
    if first_three(dna) == True and divisible(dna) == True and last_Three(dna) == True:
        return("This is an ORF")
    elif first_three(dna) == False:
        return("The first three bases are not ATG")
    elif last_Three(dna) == False:
        return("The last three bases are not a stop codon")
    else:
        return("The string is not the correct length")
    

def divisible(dna):
        if len(dna) % 3 == 0:
            return True
        else:
            return False

def first_three(dna):
    if "ATG" in dna[0:3]:
        return True
    else:
        return False
    
def last_Three(dna):
    if "TGA" in dna[-3:]:
        return True
    elif "TAG" in dna[-3:]:
        return True
    elif "TAA" in dna[-3:]:
        return True
    else:
        return False
    
def orf_starter(dna):
    x = 0
    while x <= len(dna):
        if x == len(dna):
            print("Sorry Can't Help You")
            return
        elif orf_advisor(dna[x:1]) == "This is an ORF":
            print(dna[x:])
            return
        x += 1
        

dna = ("GTTCGTTGCAACAAATT")
print(orf_advisor(dna))

dna = ("TGCTGCATGCGTAGCTAGTGG")
print(orf_advisor(dna))

dna = ("ATGGATCTAGCTGACGCTAAA")
print(orf_advisor(dna))

dna = ("ATGTGTACCCAGTCGTGTGTT")
print(orf_advisor(dna))

dna = ("ACGTATCGTAGCTATCCATT")
print(orf_starter(dna))



        