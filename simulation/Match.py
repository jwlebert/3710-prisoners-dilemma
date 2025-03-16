from typing import List, Tuple

import Strategy
from OptimizationAlgorithm import BitArrayStrategy
from Strategy import Action


class Match:
    def __init__(self, s1: Strategy, s2: Strategy, rounds=100):
        self.rounds: int = rounds
        self.round: int = 0
        self.history: List[Tuple[Action, Action]] = []

        self.p1: Strategy.Strategy = s1(self)
        self.p2: Strategy.Strategy = s2(self)
    
    def step_round(self) -> None:
        actions = (act1, act2) = self.p1.next_move(), self.p2.next_move()

        (d1, d2) = self.evaluate_round(actions)
        self.p1.score += d1
        self.p2.score += d2

        self.history.append(actions)
        self.p1.history.append(actions)
        self.p2.history.append(actions[::-1])

        self.round += 1
    
    def evaluate_round(self, actions: Tuple[Action, Action]) -> Tuple[int, int]:
        if actions == (Action.COOPERATE, Action.COOPERATE):
            return (3, 3)
        if actions == (Action.COOPERATE, Action.DEFECT):
            return (0, 5)
        if actions == (Action.DEFECT, Action.COOPERATE):
            return (5, 0)
        if actions == (Action.DEFECT, Action.DEFECT):
            return (1, 1)
        return None
    
    def simulate(self):
        for i in range(self.rounds):
            self.step_round()

class OptimizedMatch(Match):
    def __init__(self, opponent: Strategy, bit_array: int, move_depth: int, rounds=100):
        super().__init__(BitArrayStrategy, opponent, rounds=rounds)
        self.p1.set_params(bit_array, move_depth)