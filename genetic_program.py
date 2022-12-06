import random

TARGET = "Hello, world!"
POPULATION_SIZE = 100
GENERATIONS = 10000
MUTATION_RATE = 0.01

def randomString():
    string = ""
    for i in range(len(TARGET)):
        char = chr(random.randint(32, 126))
        string += char
    return string

def fitness(string):
    fitness = len(string)
    for i in range(len(string)):
        if string[i] != TARGET[i]:
            fitness -= 1
    return fitness

def selection(population):
    string1 = population[random.randint(0, len(population) - 1)]
    string2 = population[random.randint(0, len(population) - 1)]
    return string1, string2

def crossover(string1, string2):
    point = random.randint(0, len(TARGET) - 1)
    offspring1 = string1[:point] + string2[point:]
    offspring2 = string2[:point] + string1[point:]
    return offspring1, offspring2

def mutate(string):
    mutated = string
    for i in range(len(string)):
        if random.random() <= MUTATION_RATE:
            char = chr(random.randint(32, 126))
            mutated = mutated[:i] + char + mutated[i + 1:]
    return mutated

population = [randomString() for i in range(POPULATION_SIZE)]

for i in range(GENERATIONS):
    newPopulation = []
    for j in range(POPULATION_SIZE):
        string1, string2 = selection(population)
        offspring1, offspring2 = crossover(string1, string2)
        newPopulation.append(mutate(offspring1))
        newPopulation.append(mutate(offspring2))
    population = newPopulation

    print(population[0])
