from dataclasses import dataclass
from typing import Tuple

from Strategy import Strategy, Match, Action

class OptimizationAlgorithm:
    def __init__(self):
        self.iteration: int = 0

    def step():
        pass

    def generate_best_strategy() -> Strategy:
        pass

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

        move_index = self.move_index << 2 # shift by two (now there are two zeros at least significiant)
        move_index += move_bits
        
        # mask to get only the bits representing past moves
        mask = (2 ** self.move_array_size) - 1
        move_index = move_index & mask

        return move_index
    
    def next_move(self) -> Action:
        print("yes")
        if len(self.history):
            self.move_index = self.step_move_index(self.history[-1])
        
        selected_bit = 1 << self.move_index
        result = selected_bit & self.bit_array

        print(self.history[-1] if len(self.history) else None)
        print(bin(self.move_index), self.move_index, bin(self.bit_array), result)

        return Action.COOPERATE if result == 0 else Action.DEFECT