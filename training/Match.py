import Strategy

class Match:
    def __init__(self, s1: Strategy, s2: Strategy, rounds=100):
        self.rounds = rounds
        self.round = 0
        self.history = []

        self.p1 = s1(self)
        self.p2 = s2(self)
    
    def step_round(self):
        act1, act2 = self.s1.next_move(), self.s2.next_move()
        
