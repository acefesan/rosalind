import operator



dataset = open("stronghold/GC/rosalind_gc.txt","r")

S = dataset.read()
S = S.split('>')
S = S[1:]

D = {}



for entry in S:
  split = entry.split('\n')
  index = split[0]
  seq = ''.join(split[1:])
  D[index] = seq


def gc(s):
  return (s.count('G') + s.count('C'))/len(s)*100

for k in D:
  D[k] = gc(D[k])


carissawouldhavedonethisfaster= max(D.items(),key=operator.itemgetter(1))

withbettervariablenames = carissawouldhavedonethisfaster[1]

print(carissawouldhavedonethisfaster[0])
print(withbettervariablenames)

