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