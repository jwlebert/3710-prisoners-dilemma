from Model import GeneticAlgorithm

def main():
    ga = GeneticAlgorithm()
    for i in range(1001):
        if i % 10 == 0:
            print(f"Generation {i}:")
            print(f"Best : {ga.best_strategy()} {ga.best_strategy().fitness}")
            for individual in ga.population:
                print(bin(individual.chromosome), individual.fitness)
        
        ga.step()

if __name__ == "__main__":
    main()