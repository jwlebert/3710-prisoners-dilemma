from algorithms.GeneticAlgorithm import GeneticAlgorithm

def main():
    ga = GeneticAlgorithm()
    for i in range(5001):
        if i % 1000 == 0:
            print(f"Generation {i}:")
            print(f"Best : {bin(ga.best_strategy())}")
            for individual in ga.population:
                print(bin(individual.chromosome), individual.fitness)
        
        ga.step()

if __name__ == "__main__":
    main()