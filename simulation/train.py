from algorithms.GeneticAlgorithm import GeneticAlgorithm
from algorithms.HillClimbing import HillClimbing
from algorithms.TabuSearch import TabuSearch


from OptimizationAlgorithm import OptimizedTournament

def main():
    h = HillClimbing()
    s = h.train(generations=100, rounds=100)
    print(bin(s))

    ga = GeneticAlgorithm(memory_depth=3, pop_size=1000, mutation_rate=0.1)
    s = ga.train(generations=500, rounds=100)
    print(bin(s))

    ts = TabuSearch(memory_depth=3, tabu_len=100)
    s = ts.train(generations=250, rounds=100)
    print(bin(s))


if __name__ == "__main__":
    main()
