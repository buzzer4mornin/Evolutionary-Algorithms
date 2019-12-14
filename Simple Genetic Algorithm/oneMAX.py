import random
import utils
import functools
import matplotlib.pyplot as plt

# =======================================FUNCTIONS============================================

#creates individual based with input of individual length
def create_ind(ind_len):  
    return [random.randrange(0, 2) for _ in range(ind_len)]

#creates population with input of population size and individual size
def create_pop(pop_size,indiv_len):
    return [create_ind(indiv_len) for _ in range(pop_size)]

#evaluates and returns fitness value of individual
def fitness(individual):
  num=0
  for i in individual:
    if i==1:
      num+=1
  return num

#performs crossover on two parent individuals and returns two new child individual
def one_pt_cross(p1, p2):
    point = random.randrange(1, len(p1))
    o1 = p1[:point] + p2[point:]
    o2 = p2[:point] + p1[point:]
    return o1, o2

#performs crossover based on probability. Links to other crossover function    
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

oneMAXbefore = 0
for sample in population:
  if 0 not in sample:
    oneMAXbefore +=1
print("# of oneMAX before =",oneMAXbefore)

populationcopy = population #copy original population, it will be helpful later


for G in range(100):
   
  fitness_indv = list(map(fitness, population))   #evaluate fitness values of individuals inside population   
  firsthighestN = sorted(range(len(fitness_indv)), key = lambda sub: fitness_indv[sub])[-N:] #sort the fitness values and returns indices of first highest N numbers 
  crossindicies_list = list(firsthighestN)
  crossindv_list = []
  for i in crossindicies_list:
    crossindv_list.append(population[i])
  aftercrossindv_list = crossover(crossindv_list,one_pt_cross,crossover_prob)
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
  newlist = aftercrossindv_list+aftermutationlist_indv
  random.shuffle(newlist)
  oneMAXafter = 0
  for sample in newlist:
    if 0 not in sample:
      oneMAXafter +=1  
  population = newlist
print("# of oneMAX after",G,"th iteration =",oneMAXafter)  

