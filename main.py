## Importing Dependencies
from random import randint,shuffle

## Setting The Problem and Algorithm Parameters

N :int = 4
PS:int = 6 # Population Size
MR = 0.8 # Mutation Rate

## Initial Population Function

def init_population(n:int, ps:int) -> list:
    population_list = list()
    for _ in range(ps):
        member = list()
        for _ in range(n):
            member.append(randint(0,n-1))
        population_list.append(member+[None])

    return population_list

## Cross-Over Function
def cross_over(population_list:list, n:int, ps:int) -> list:
    for i in range(0,ps,2):
        child1 = population_list[i][:n//2]+population_list[i+1][n//2:n]+[None]
        child2 = population_list[i+1][:n//2]+population_list[i][n//2:n]+[None]
        population_list.append(child1)
        population_list.append(child2)
    return population_list

## Mutation Function
def mutation(population_list, n:int, ps:int, mr:float):
    choosen_ones = list(range(ps,ps*2))
    shuffle(choosen_ones)
    choosen_ones = choosen_ones[:int(ps*mr)]
    print(choosen_ones,'choosen')
    
    
    for i in choosen_ones:
        cell = randint(0,n-1)
        val = randint(0,n-1)
        population_list[i][cell]=val
    return population_list

## Main

current_population : list = init_population(N, PS)

current_population = cross_over(current_population, N, PS)
print(current_population[PS:],'z')
current_population = mutation(current_population, N, PS, MR)
print(current_population[PS:],'p')
