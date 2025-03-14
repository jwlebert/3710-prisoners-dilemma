from enum import Enum
from typing import List
import Match

class Action(Enum):
    COOPERATE = 0
    DEFECT = 1

class Strategy:
    def __init__(self, match: Match):
        self.match: Match = match
        self.score: int = 0
        self.opp_history: List[int] = []

    def next_move(self) -> Action:
        pass

class AlwaysCooperate(Strategy):
    def next_move(self):
        return Action.COOPERATE