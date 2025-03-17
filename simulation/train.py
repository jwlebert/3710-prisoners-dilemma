from algorithms.GeneticAlgorithm import GeneticAlgorithm
from algorithms.HillClimbing import HillClimbing

def main():
    h = HillClimbing()
    s = h.train(generations=100, rounds=20)
    print(bin(s))

    ga = GeneticAlgorithm(memory_depth=3, pop_size=100, mutation_rate=0.001)
    s = ga.train(generations=100, rounds=20)
    print(bin(s))

if __name__ == "__main__":
    main()