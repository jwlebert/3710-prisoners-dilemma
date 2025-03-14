import itertools
import matplotlib.pyplot

strategies = []

def tournament (strategies, rounds=100):
    results = {}

    for strat1, strat2 in intertools.combinations(strategies, 2):
        game = IteratedPrisoners Dilemma(strat1, strat2, rounds)
        score1, score2 = game.play()

        results[(strat1.name, strat2.name)] = (score1, score2)

    return results