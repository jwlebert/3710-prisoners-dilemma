from Match import Match
import Strategy

def main():
    match = Match(Strategy.AlwaysCooperate, Strategy.AlwaysCooperate, rounds=5)
    match.simulate()

    print(*match.history, sep="\n")
    print(match.p1.score, match.p2.score)


if __name__ == "__main__":
    main()