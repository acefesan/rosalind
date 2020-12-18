
def read_fasta(filename):
  dataset = open(filename,"r")
  S = dataset.read()
  S = S.split('>')
  S = S[1:]

  D = {}
  for entry in S:
    split = entry.split('\n')
    index = split[0]
    seq = ''.join(split[1:])
    D[index] = seq

  return D


entries = read_fasta("stronghold/GRPH/rosalind_grph.txt")


def is_connected(s,t):
  return s[-3:] == t[:3]


with open("stronghold/GRPH/out.txt",'a') as out:

  for e in entries.keys():
    for i in entries.keys():
     s = entries[e]
     t = entries[i]
     if s != t:
      if is_connected(s,t):
        out.write(e +' '+i+'\n')

  out.close()
