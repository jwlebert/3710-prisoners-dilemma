from enum import Enum
from typing import List, Tuple
import random

import Match

class Action(Enum):
    COOPERATE = 0
    DEFECT = 1

class Strategy:
    def __init__(self, match: Match):
        self.match: Match = match
        self.score: int = 0
        self.history: List[Action] = [] # (player, opponent) <- move format

    def next_move(self) -> Action:
        pass

class AlwaysCooperate(Strategy):
    def next_move(self):
        return Action.COOPERATE

class AlwaysDefect(Strategy):
    def next_move(self):
        return Action.DEFECT

class TitForTat(Strategy):
    def next_move(self):
        if len(self.history) == 0:
            return Action.COOPERATE
        else:
            return self.history[-1][1]
        
class SuspiciousTitForTat(Strategy):
    def next_move(self):
        if len(self.history) == 0:
            return Action.DEFECT
        else:
            return self.history[-1][1]

class Random(Strategy):
    def next_move(self):
        return random.choice([Action.DEFECT, Action.COOPERATE])

class TitFor2Tat(Strategy):
    def next_move(self):
        if len(self.history) < 2:
            return Action.COOPERATE
        elif (
            self.history[-1][1] == Action.DEFECT
            and self.history[-2][1] == Action.DEFECT
        ):
            return Action.DEFECT
        else:
            return Action.COOPERATE


class GenerousTitForTat(Strategy):
    def next_move(self):
        if len(self.history) == 0:
            return Action.COOPERATE
        # Forgive with probability of 0.1 (generally considered good in research)
        elif self.history[-1][1] == Action.DEFECT:
            if random.random() < 0.1:
                return Action.COOPERATE
            else:
                return Action.DEFECT
        else:
            return Action.COOPERATE

class Pavlov(Strategy):
    def next_move(self):
        if len(self.history) == 0:
            return Action.COOPERATE
        elif self.history[-1][0] == self.history[-1][1]:
            return self.history[-1][0]
        elif self.history[-1][1] == Action.DEFECT:
            return Action.DEFECT
        else:
            return Action.COOPERATE