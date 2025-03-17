from algorithms.GeneticAlgorithm import GeneticAlgorithm
from algorithms.HillClimbing import HillClimbing

def main():
    ga = GeneticAlgorithm(memory_depth=3, pop_size=100, mutation_rate=0.001)
    s = ga.train(generations=100)
    print(bin(s))

if __name__ == "__main__":
    main()