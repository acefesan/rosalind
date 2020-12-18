residues = open("stronghold/PRTM/residue_dict.txt","r")

residues = [res.strip().split('  ') for res in residues.readlines()]
residuesMass = {}
for res in residues:
  residuesMass[res[0]] = float(res[1])

dataset = open("stronghold/PRTM/rosalind_prtm.txt","r")


prot = dataset.read().strip()
mass = 0
for p in prot:
  mass += residuesMass[p]

print(mass)