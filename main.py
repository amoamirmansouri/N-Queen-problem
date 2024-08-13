## Importing Dependencies
from random import randint,shuffle

## Setting The Problem and Algorithm Parameters

N :int = 4
PS:int = 6 # Population Size
MR = 0.8 # Mutation Rate
EPOCH = 200

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
def cross_over(population_list, n:int, ps:int) -> list:
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
    
    
    
    for i in choosen_ones:
        cell = randint(0,n-1)
        val = randint(0,n-1)
        population_list[i][cell]=val
    return population_list

## Fitness Function

def fitness(population_list, n:int) -> list:
    length:int = len(population_list)
    for i in range(length):
        conflict = 0
        for j in range(n):
            for k in range(j+1,n):
            # column
                if population_list[i][j] == population_list[i][k]:
                    conflict+=1
            # diagonal
                if abs(j-k) == abs(population_list[i][j]-population_list[i][k]):
                    conflict+=1
                
        population_list[i][-1] = conflict
    return population_list
    

## Main
current_population : list = init_population(N, PS)
current_population = fitness(current_population, N)
current_population = sorted(current_population, key=lambda x:x[-1])
if current_population[0][-1] == 0:
    print("Solutin is found in the initial population stae", current_population[0])
else:
    for i in range(EPOCH):

        current_population = cross_over(current_population, N, PS)

        current_population = mutation(current_population, N, PS, MR)

        current_population = fitness(current_population, N)

        current_population = sorted(current_population, key=lambda x:x[-1])

        current_population = current_population[:PS]

        if current_population[0][-1] == 0: 
            print(i+1,"Solution Found", current_population[0])
            break

        else:
            print(i+1,"best solution so far", current_population[0])

    else:
        print("Sorry, we could not find you a solution!!!")