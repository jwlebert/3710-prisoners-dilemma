import random
from typing import List


class Model:
    pass

class GeneticIndividual: # individual agent
    def __init__(self, chromosome: int):
        self.chromosome: int = chromosome
        self.fitness: int = 0

class GeneticAlgorithm(Model): # population
    def __init__(self, pop_size: int = 20, mutation_rate: float = 0.001, memory_depth: int = 3):
        self.population: List[GeneticIndividual] = []
        self.pop_size: int = pop_size
        self.mutation_rate: float = mutation_rate
        self.memory_depth: int = memory_depth
        self.gene_bit_len: int = 2 ** (2 * memory_depth) # number of bits in chromosomes
    
    def initial_sample(self):
        new_pop = []
        for _ in range(self.pop_size):
            chromosome = random.randint(0, (2 ** self.gene_bit_len) - 1)
            new_pop.append(GeneticIndividual(chromosome))
        
        self.population = new_pop

    def select_parents(self): # roulette wheel selection
        total_fitness = 0
        for individual in self.population:
            total_fitness += individual.fitness

        # here we combine probability calculation and selection for efficiency
        prob1, p1 = random.random(), None # parent 1 prob
        prob2, p2 = random.random(), None # parent 2 prob

        cumulative: float = 0.0
        for individual in self.population:
            prob: float = individual.fitness / total_fitness
            cumulative += prob
            
            if p1 is None and cumulative >= prob1:
                p1 = individual
            if p2 is None and cumulative >= prob2:
                p2 = individual

            if p1 is not None and p2 is not None:
                break
        
        return (p1, p2)
    
    def mutate(self, individual: GeneticIndividual):
        mutated_chromosome = individual.chromosome
        for i in range(self.gene_bit_len):
            if (random.random > self.mutation_rate): continue

            bit = 1 << i
            mutated_chromosome = mutated_chromosome ^ bit
        individual.chromosome = mutated_chromosome