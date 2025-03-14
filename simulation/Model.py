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