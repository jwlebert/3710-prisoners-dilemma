from algorithms.GeneticAlgorithm import GeneticAlgorithm

def main():
    ga = GeneticAlgorithm(pop_size=100, mutation_rate=0.001, memory_depth=3)
    s = ga.train(generations=100)
    print(bin(s))

if __name__ == "__main__":
    main()