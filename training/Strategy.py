class Strategy:
    def __init__(self, match):
        self.match = match
        self.score = 0

    def next_move(self):
        pass

class AlwaysCooperate(Strategy):
    pass