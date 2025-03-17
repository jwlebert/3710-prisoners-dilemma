from algorithms.GeneticAlgorithm import GeneticAlgorithm
import matplotlib.pyplot as plt

def GeneticOptimization():
    ga = GeneticAlgorithm(pop_size=100, mutation_rate=0.001, memory_depth=3)
    ga.train(generations=100)
    genetic_strategy = ga.best_strategy()
    return genetic_strategy
