"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

D = {'C': 'G', 'G':'C', 'A':'T', 'T':'A'}

dataset = open("stronghold/REVC/rosalind_revc.txt","r")

S = dataset.readlines()[0]
S = S.strip()

out = ""
for nt in S[::-1]:
  out += (D[nt])
  
print(out)