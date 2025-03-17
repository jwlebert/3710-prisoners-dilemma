import random
from typing import List, Tuple

from OptimizationAlgorithm import OptimizationAlgorithm, OptimizedTournament

class GeneticIndividual: # individual agent
    def __init__(self, chromosome: int, memory_depth: int, rounds: int):
        self.chromosome: int = chromosome
        self.memory_depth: int = memory_depth
        self.rounds: int = rounds
        self.__fitness: int = None
    
    @property
    def fitness(self):
        if self.__fitness is None:
            tournament = OptimizedTournament(self.chromosome, self.memory_depth, rounds=self.rounds)
            self.__fitness = tournament.get_score()
        
        return self.__fitness

class GeneticAlgorithm(OptimizationAlgorithm): # population
    def __init__(self, memory_depth: int = 3, pop_size: int = 20, mutation_rate: float = 0.001):
        super().__init__(memory_depth=memory_depth)
        
        self.population: List[GeneticIndividual] = []
        self.pop_size: int = pop_size # best when even
        self.mutation_rate: float = mutation_rate
    
    def initial_sample(self):
        new_pop = []
        for _ in range(self.pop_size):
            chromosome = random.randint(0, (2 ** self.bit_arr_len) - 1)
            new_pop.append(GeneticIndividual(chromosome, self.memory_depth, self.rounds))
        
        self.population = new_pop

    def step(self, rounds: int) -> None:
        if not len(self.population):
            self.rounds = rounds
            self.initial_sample()
            
        next_generation = []

        for _ in range(0, self.pop_size // 2):
            parents = self.select_parents()
            c1, c2 = self.crossover(parents)

            c1.chromosome = self.mutate(c1)
            c2.chromosome = self.mutate(c2)

            next_generation.append(c1)
            next_generation.append(c2)
        
        self.population = next_generation
        self.iteration += 1

        return None
    
    def best_strategy(self):
        best_individual: GeneticIndividual = sorted(self.population, key=lambda l: l.fitness, reverse=True)[0]
        return best_individual.chromosome

    def select_parents(self) -> Tuple[GeneticIndividual, GeneticIndividual]: # roulette wheel selection
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

    # random point crossover
    def crossover(self, parents: Tuple[GeneticIndividual, GeneticIndividual]) -> Tuple[GeneticIndividual, GeneticIndividual]:
        p1, p2 = parents

        crossover_index = random.randint(1, self.bit_arr_len - 1)
        crossover_mask = (1 << crossover_index) - 1

        chromo1 = (p1.chromosome & ~crossover_mask) | (p2.chromosome & crossover_mask)
        chromo2 = (p2.chromosome & ~crossover_mask) | (p1.chromosome & crossover_mask)

        c1 = GeneticIndividual(chromo1, self.memory_depth, self.rounds)
        c2 = GeneticIndividual(chromo2, self.memory_depth, self.rounds)

        return (c1, c2)
    
    def mutate(self, individual: GeneticIndividual) -> int:
        mutated_chromosome = individual.chromosome
        for i in range(self.bit_arr_len):
            if (random.random() > self.mutation_rate): continue

            bit = 1 << i
            mutated_chromosome = mutated_chromosome ^ bit
        return mutated_chromosome