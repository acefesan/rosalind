from codonDict import rnaCodonDict

dataset = open("stronghold/PROT/rosalind_prot.txt","r")



S = dataset.readlines()[0].strip()
out = ""
for i in range(0,len(S),3):
  out += rnaCodonDict[S[i:i+3]]

print(out.strip('*'))