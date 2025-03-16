from enum import Enum
from typing import List
import random

import Match


class Action(Enum):
    COOPERATE = 0
    DEFECT = 1


class Strategy:
    def __init__(self, match: Match):
        self.match: Match = match
        self.score: int = 0
        self.opp_history: List[Action] = []

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
        if len(self.opp_history) == 0:
            return Action.COOPERATE
        else:
            return self.opp_history[-1]


class TitFor2Tat(Strategy):
    def next_move(self):
        if len(self.opp_history) < 2:
            return Action.COOPERATE
        elif (
            self.opp_history[-1] == Action.DEFECT
            and self.opp_history[-2] == Action.DEFECT
        ):
            return Action.DEFECT
        else:
            return Action.COOPERATE


class SuspiciousTitForTat(Strategy):
    def next_move(self):
        if len(self.opp_history) == 0:
            return Action.DEFECT
        else:
            return self.opp_history[-1]


class Random(Strategy):
    def next_move(self):
        return random.choice([Action.DEFECT, Action.COOPERATE])
