import random

# =======================================FUNCTIONS============================================
def create_ind(ind_len):
    return [random.randrange(0, 2) for _ in range(ind_len)]

def create_pop(pop_size,indiv_len):
    return [create_ind(indiv_len) for _ in range(pop_size)]

def fitness(individual):
  sequence=0
  for i,j in zip(range(len(individual)-1),range(len(individual))):
    j+=1
    if individual[i]!=individual[j]:
     sequence +=1
  return sequence

def one_pt_cross(p1, p2):
    point = random.randrange(1, len(p1))
    o1 = p1[:point] + p2[point:]
    o2 = p2[:point] + p1[point:]
    return o1, o2

def crossover(pop, cross, cx_prob):
    off = []
    for p1, p2 in zip(pop[0::2], pop[1::2]):
        if random.random() < cx_prob:
            o1, o2 = cross(p1, p2)
        else:
            o1, o2 = p1[:], p2[:]
        off.append(o1)
        off.append(o2)
    return off

# =======================================INITIALIZE VALUES============================================

individual_length = 10
crossover_prob = 0.8 
mutation_prob = 0.1
population_size=100
N= (int)(0.6*population_size) 

population=create_pop(population_size,individual_length) 
populationcopy = population 
#==========
notalternating=0
for indv in population:
    for i,j in zip(range(len(indv)-1),range(len(indv))):
       j+=1
       if indv[i]==indv[j]:
          notalternating +=1
          break
          
alternating = population_size - notalternating
print("# of alternating individuals BEFORE RUN=",alternating)
#==========

for G in range(200):
  fitness_indv = list(map(fitness, population)) 
  firsthighestN = sorted(range(len(fitness_indv)), key = lambda sub: fitness_indv[sub])[-N:]
  crossindicies_list = list(firsthighestN)
  crossindv_list = []
  beforecross_fits=[]
  for i in crossindicies_list:
    crossindv_list.append(population[i])
  aftercrosslist_indv = crossover(crossindv_list,one_pt_cross,crossover_prob)
  mutationindicies_list = []
  totallist=list(range(population_size))
  for element in totallist:
    if element not in crossindicies_list:
        mutationindicies_list.append(element)
  initialmutation_population = []
  for i in mutationindicies_list:
    initialmutation_population.append(population[i])
  aftermutationlist_indv = []
  for i in mutationindicies_list:
    sample = populationcopy[i]
    for j in range(len(sample)):
      if random.random()< mutation_prob:
       if sample[j]==1:
          sample[j]=0
       else:
         sample[j]=1  
    aftermutationlist_indv.append(sample)
  newlist = aftercrosslist_indv+aftermutationlist_indv
  random.shuffle(newlist)
  population = newlist
  notalternating1=0
  for indv in newlist:
      for i,j in zip(range(len(indv)-1),range(len(indv))):
       j+=1
       if indv[i]==indv[j]:
          notalternating1 +=1
          break
          
  alternating = population_size - notalternating1
 
#==========================================================================  
print("# of alternating individuals AFTER RUN=",alternating)
result = []
for individual in population:
  a = fitness(individual)
  if a==9:
    result.append(individual)
print("Alternating individuals AFTER:",result)