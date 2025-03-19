import random
from OptimizationAlgorithm import OptimizationAlgorithm, OptimizedTournament

class HillClimbingRandomRestart(OptimizationAlgorithm):
    def __init__(self, num_restarts: int = 50, memory_depth: int = 3, rounds: int = 50):
        super().__init__(memory_depth=memory_depth, rounds=rounds)

        self.num_restarts: int = num_restarts
        # random start
        self.bit_arr: int = random.randint(0, (2 ** self.bit_arr_len) - 1)
        self.fitness: float = None

    def step(self, rounds: int):
        if self.fitness is None:
            self.fitness = self.evaluate(self.bit_arr, rounds)

        evaluated_neighbors = [(n, self.evaluate(n, rounds)) for n in neighbours]
        max_neighbour, highest_fitness = max(evaluated_neighbors, key=lambda x: x[1])

        max_neighbour = max(neighbours, key=lambda n: self.evaluate(n, rounds))
        highest_fitness = self.evaluate(max_neighbour, rounds)

        if highest_fitness <= self.fitness:
            if (self.fitness > self.global_best[1]):
                self.global_best = (self.bit_arr, self.fitness)
            if self.num_restarts > 0:
                self.num_restarts -= 1

                self.bit_arr = random.randint(0, (2 ** self.bit_arr_len) - 1)
                self.fitness = None

                return None
        
        self.bit_arr = max_neighbour
        self.fitness = highest_fitness
        
        self.iteration += 1

        return None
    
    def best_strategy(self):
        return self.global_best[0]
        
    def evaluate(self, bit_arr, rounds):
        tournament = OptimizedTournament(bit_arr, self.memory_depth, rounds=rounds)
        return tournament.get_score()

    def bit_flip(self, bit_index: int) -> int:
        return self.bit_arr ^ (1 << bit_index)