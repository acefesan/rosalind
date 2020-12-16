dataset = open("stronghold/FIBD/rosalind_fibd.txt","r")

ls = dataset.readlines()[0].strip().split(' ')

n = int(ls[0])
m = int(ls[1])

pop = [0 for x in range(m)]
pop[0] = 1

print("Gen 1", pop)

for i in range(1,n):
  tmp = sum(pop[1:])
  pop[1:] = pop[0:-1]
  pop[0] = tmp
  #print("Gen",i+1,pop)

print(sum(pop))