

dataset = open("stronghold/IEV/rosalind_iev.txt","r")

nums = dataset.readlines()[0].strip().split(' ')

Dprob = {
"AA-AA":2,
"AA-Aa":2,
"AA-aa":2,
"Aa-Aa":2*0.75,
"Aa-aa":2*0.5,
"aa-aa":0
}

D = {}

for k,num in zip(Dprob.keys(),nums):
  D[k] = int(num)*Dprob[k]

print(sum(D.values()))