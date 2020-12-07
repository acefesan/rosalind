"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

D = {'A': 'A', 'C':'C', 'G':'G', 'T':'U'}

dataset = open("stronghold/IPRB/rosalind_iprb.txt","r")

S = dataset.readlines()[0]
S = S.strip().split(' ')

k = float(S[0])
m = float(S[1])
n = float(S[2])

print(k)
print(m)
print(n)

N = k + m + n
succ = N-1

D = k/N

MD = (m/N)*(k/succ)
MM = (m/N)*((m-1)/succ)*0.75
MR = (m/N)*(n/succ) * 0.5
RD = (n/N)*(k/succ)
RM = (n/N)*(m/succ)*0.5

print(D+MD+MM+MR+RD+RM)


