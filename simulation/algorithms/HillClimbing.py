import random
from OptimizationAlgorithm import OptimizationAlgorithm, OptimizedTournament

class HillClimbing(OptimizationAlgorithm):
    def __init__(self, memory_depth: int = 3, rounds: int = 50):
        super().__init__(memory_depth=memory_depth, rounds=rounds)

        # random start
        self.bit_arr: int = random.randint(0, (2 ** self.bit_arr_len) - 1)
        self.fitness: float = None

    def step(self, rounds: int):
        if self.fitness is None:
            self.fitness = self.evaluate(self.bit_arr, rounds)

        evaluated_neighbors = [(n, self.evaluate(n, rounds)) for n in neighbours]
        max_neighbour, highest_fitness = max(evaluated_neighbors, key=lambda x: x[1])

        if highest_fitness <= self.fitness:
            return self.iteration
        
        self.bit_arr = max_neighbour
        self.fitness = highest_fitness
        
        self.iteration += 1

        return None
    
    def best_strategy(self):
        return self.bit_arr
        
    def evaluate(self, bit_arr, rounds):
        tournament = OptimizedTournament(bit_arr, self.memory_depth, rounds=rounds)
        return tournament.get_score()

    def bit_flip(self, bit_index: int) -> int:
        return self.bit_arr ^ (1 << bit_index)
