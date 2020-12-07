"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

"""

dataset = open("stronghold/FIB/rosalind_fib.txt","r")

S = dataset.readlines()[0]
S = S.strip().split(' ')

n = int(S[0])
k = int(S[1])



a1 = 1
a2 = 1

for i in range(2,n):
  an = a2 + a1*k
  a1 = a2
  a2 = an


print(an)