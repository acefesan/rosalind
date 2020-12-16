import functools

rnaCodonDict = {
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'UUA': 'L', 'UUG': 'L',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UUU': 'F', 'UUC': 'F', 'AUG': 'M', 'UGU': 'C', 'UGC': 'C',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'CCU': 'P',
    'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'UCU': 'S', 'UCC': 'S',
    'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UGG': 'W', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'CAU': 'H', 'CAC': 'H', 'GAA': 'E', 'GAG': 'E', 'GAU': 'D', 'GAC': 'D', 'AAA': 'K',
    'AAG': 'K', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R', 'UAA': '*', 'UAG': '*',
    'UGA': '*'
}

D = {}

vals = list(rnaCodonDict.values())
for p in set(rnaCodonDict.values()):
  D[p] = vals.count(p)

print(D)



dataset = open("stronghold/MRNA/rosalind_mrna.txt","r")

prot = dataset.read().strip()
print(prot)
a = [D[x] for x in prot]
numCombinations = functools.reduce(lambda x,y: (x*y)%1000000, a) * 3 # *3 for stop codon

print(numCombinations)
