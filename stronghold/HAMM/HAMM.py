dataset = open("stronghold/HAMM/rosalind_hamm.txt","r")

S = dataset.readlines()
S = [s.strip() for s in S]

s = S[1]
S = S[0]


out = 0
for i in range(len(S)):
  if(S[i] != s[i]):
    out += 1
  
  
  
print(out)