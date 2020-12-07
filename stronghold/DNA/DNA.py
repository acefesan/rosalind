""" 
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


"""

D = {'A': 0, 'C':0, 'G':0, 'T':0}

dataset = open("stronghold/DNA/rosalind_dna.txt","r")

S = dataset.readlines()[0]
S = S.strip()

for s in S:
  D[s] += 1

out = ""
for nt in D:
  out += (str(D[nt]) + ' ')
  
print(out)
