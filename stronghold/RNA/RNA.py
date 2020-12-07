"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

D = {'A': 'A', 'C':'C', 'G':'G', 'T':'U'}

dataset = open("stronghold/RNA/rosalind_rna.txt","r")

S = dataset.readlines()[0]
S = S.strip()

out = ""
for nt in S:
  out += (D[nt])
  
print(out)