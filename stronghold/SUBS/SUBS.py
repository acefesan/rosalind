

dataset = open("stronghold/SUBS/rosalind_subs.txt","r")

S = dataset.readlines()
S = [s.strip() for s in S]

s = S[1]
S = S[0]


out = ''
for i in range(len(S)):
  sls = S[i:(i+len(s))]
  if sls == s:
    out += (str(i+1) + ' ')
  
  
print(out)