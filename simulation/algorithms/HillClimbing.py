import random
from OptimizationAlgorithm import OptimizationAlgorithm, OptimizedTournament

class HillClimbing(OptimizationAlgorithm):
    def __init__(self, memory_depth: int = 3, rounds: int = 50):
        super().__init__(memory_depth=memory_depth, rounds=rounds)

        # random start
        self.bit_arr: int = random.randint(0, (2 ** self.bit_arr_len) - 1)
        tournament = OptimizedTournament(self.bit_arr, self.memory_depth, rounds=50)
        self.fitness = tournament.get_score()

    def step(self):
        neighbours = [self.bit_flip(i) for i in range(self.bit_arr_len)]
        for n in neighbours: print(n, self.evaluate(n))

        max_neighbour = max(neighbours, key=lambda n: self.evaluate(n))
        highest_fitness = self.evaluate(max_neighbour)

        if highest_fitness <= self.fitness:
            return self.iteration
        
        self.bit_arr = max_neighbour
        self.fitness = highest_fitness
        
        self.iteration += 1

        return None
        
    def evaluate(self, bit_arr):
        tournament = OptimizedTournament(bit_arr, self.memory_depth, rounds=50)
        return tournament.get_score()

    def bit_flip(self, bit_index: int) -> int:
        return self.bit_arr ^ (1 << bit_index)
