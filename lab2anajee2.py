# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

DNA = ("A", "T", "C", "G")

aDNA = DNA[0] * 10
tDNA = DNA[1] * 20
cDNA = DNA[2] * 30
gDNA = DNA[3] * 40

c = len(aDNA) + len(tDNA) + len(cDNA) + len(gDNA)

print("The total length of the DNA string is {}".format(c))


if aDNA + tDNA > cDNA + gDNA:
    print("True")
else:
    print("False")
    
    
