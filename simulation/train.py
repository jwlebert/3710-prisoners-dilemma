from algorithms.GeneticAlgorithm import GeneticAlgorithm
from algorithms.HillClimbing import HillClimbing

from OptimizationAlgorithm import OptimizedTournament

def main():
    ga = GeneticAlgorithm(memory_depth=3, pop_size=150, mutation_rate=0.01)
    s = ga.train(generations=5000, rounds=100, log_freq=250, logging=True)
    print(bin(s))

    t = OptimizedTournament(s, 3, 100)
    print(t.get_score())


if __name__ == "__main__":
    main()