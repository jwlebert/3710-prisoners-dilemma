from Match import Match, OptimizedMatch
import Strategy
from OptimizationAlgorithm import BitArrayStrategy

def main():
    match = Match(Strategy.AlwaysCooperate, Strategy.AlwaysCooperate, rounds=5)
    match.simulate()

    print(*match.history, sep="\n")
    print(match.p1.score, match.p2.score)

    match = Match(Strategy.AlwaysDefect, Strategy.TitForTat, rounds=5)
    match.simulate()

    print(*match.history, sep="\n")
    print(match.p1.score, match.p2.score)

    match = Match(Strategy.Random, Strategy.SuspiciousTitForTat, rounds=5)
    match.simulate()

    print(*match.history, sep="\n")
    print(match.p1.score, match.p2.score)

    match = OptimizedMatch(Strategy.AlwaysCooperate, 3, 1, rounds=5)
    match.simulate()

    print(*match.history, sep="\n")
    print(match.p1.score, match.p2.score)


if __name__ == "__main__":
    main()