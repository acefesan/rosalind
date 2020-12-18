from scipy.stats import binom

dataset = open("stronghold/LIA/rosalind_lia.txt","r")

S = dataset.readlines()[0]
S = S.strip().split(' ')

k = int(S[0])
N = int(S[1])


print("generations:",k)
print("number of double heterozygotes:",N)
print("population at gen k:",2**k)

print(1-binom.cdf(N-1,2**k,0.25))