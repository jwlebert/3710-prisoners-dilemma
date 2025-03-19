from typing import Tuple
from Match import Match
from Strategy import Action, Strategy

from Strategy import (
    AlwaysCooperate,
    AlwaysDefect,
    TitForTat,
    TitFor2Tat,
    SuspiciousTitForTat,
    Random,
    GenerousTitForTat,
    Pavlov,
    GrimTrigger,
    Prober
)

strategies = [
    AlwaysCooperate,
    AlwaysDefect,
    TitForTat,
    TitFor2Tat,
    SuspiciousTitForTat,
    Random,
    GenerousTitForTat,
    Pavlov,
    GrimTrigger,
    Prober
]


class BitArrayStrategy(Strategy):
    def __init__(self, match: Match, move_depth: int = 1, bit_array: int = 0):
        super().__init__(match)
        self.set_params(bit_array, move_depth)

    def set_params(self, bit_array: int, move_depth: int):
        self.move_depth: int = move_depth
        self.move_array_size: int = move_depth * 2
        self.bit_array_size: int = 2 ** (self.move_array_size)

        self.bit_array: int = bit_array
        self.move_index: int = 0

    def step_move_index(self, move: Tuple[Action, Action]) -> int:
        move_bits = 2 * move[0].value + move[1].value

        move_index = (
            self.move_index << 2
        )  # shift by two (now there are two zeros at least significiant)
        move_index += move_bits

        # mask to get only the bits representing past moves
        mask = (2**self.move_array_size) - 1
        move_index = move_index & mask

        return move_index

    def next_move(self) -> Action:
        if len(self.history):
            self.move_index = self.step_move_index(self.history[-1])

        selected_bit = 1 << self.move_index
        result = selected_bit & self.bit_array

        return Action.COOPERATE if result == 0 else Action.DEFECT


class OptimizationAlgorithm:
    def __init__(self, memory_depth: int = 3, rounds: int = 50):
        self.iteration: int = 0
        
        self.rounds: int = rounds
        self.memory_depth: int = memory_depth
        self.bit_arr_len: int = 2 ** (2 * memory_depth)
        self.global_best = (None, 0)

    def step(self, rounds: int):
        pass

    def best_strategy() -> int:
        pass

    def train(self, generations: int, rounds: int, logging: bool = False, log_freq: int = 100) -> BitArrayStrategy:
        if not logging:
            for _ in range(generations + 1): 
                if self.step(rounds) is not None:
                    print(self.iteration)
                    return self.best_strategy()
        else:
            for gen in range(generations + 1):
                if gen % log_freq == 0:
                    print(gen)

                if self.step(rounds) is not None:
                    return self.best_strategy()
        
        return self.best_strategy()


class OptimizedMatch(Match):
    def __init__(
        self, opponent: Strategy, bit_array: int, move_depth: int = 3, rounds: int = 100
    ):
        super().__init__(BitArrayStrategy, opponent, rounds=rounds)
        self.p1.set_params(bit_array, move_depth)


class OptimizedTournament:
    def __init__(self, bit_array: int, move_depth: int, rounds: int = 100):
        self.bit_array: int = bit_array
        self.move_depth: int = move_depth
        self.rounds: int = rounds

    def get_score(self):
        score: int = 0
        for opp in strategies:
            match = OptimizedMatch(
                opp, self.bit_array, self.move_depth, rounds=self.rounds
            )
            match.simulate()
            score += match.p1.score / self.rounds

        return score / len(strategies)
