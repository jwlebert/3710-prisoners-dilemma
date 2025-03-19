import random
from OptimizationAlgorithm import OptimizationAlgorithm, OptimizedTournament

class TabuSearch(OptimizationAlgorithm):
    def __init__(self, memory_depth: int = 3, tabu_len: int = 100, rounds: int = 50):
        super().__init__(memory_depth=memory_depth, rounds=rounds)

        # random start
        self.bit_arr: int = random.randint(0, (2 ** self.bit_arr_len) - 1)
        self.fitness: float = None

        self.tabu = []
        self.tabu_len = tabu_len

    def step(self, rounds: int):
        if self.fitness is None:
            self.fitness = self.evaluate(self.bit_arr, rounds)

        neighbours = [self.bit_flip(i) for i in range(self.bit_arr_len) if self.bit_flip(i) not in self.tabu]

        if len(neighbours):
            evaluations = [(n, self.evaluate(n, rounds)) for n in neighbours]
            max_neighbour, highest_fitness = max(evaluations, key=lambda x: x[1])
        else:
            return self.iteration
        
        self.bit_arr = max_neighbour
        self.fitness = highest_fitness

        if self.fitness > self.global_best[1]:
            self.global_best = (self.bit_arr, self.fitness)

        self.tabu.append(max_neighbour)
        self.tabu = self.tabu[0:self.tabu_len]
        
        self.iteration += 1

        return None
    
    def best_strategy(self):
        return self.global_best[0]
        
    def evaluate(self, bit_arr, rounds):
        tournament = OptimizedTournament(bit_arr, self.memory_depth, rounds=rounds)
        return tournament.get_score()

    def bit_flip(self, bit_index: int) -> int:
        return self.bit_arr ^ (1 << bit_index)
