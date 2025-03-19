# %%
import itertools
import matplotlib.pyplot as plot
import pandas as pd
import seaborn as sns

from Match import Match


from OptimizationAlgorithm import BitArrayStrategy


def tournament(strategies, rounds=100):
    results = {}

    strategies = [(x, x.__name__) for x in strategies]  # turn them all into tuples

    # print(strategies)
    # Get best genetic algorithm strategy
    genetic_strat = 0b11100100111000111111011010111101110010100101010011111011101000
    hill_climb_strat = 0b10100100011011000111111000101011100011101100000111000110011001
    tabu_strat = 0b1111011111100011000001101010110011010001000000100111011001011100

    strategies.append(
        (
            BitArrayStrategy,
            "GeneticAlgorithm",
            genetic_strat,
            3,
        )
    )

    strategies.append(
        (
            BitArrayStrategy,
            "HillClimbing",
            hill_climb_strat,
            3,
        )
    )

    strategies.append(
        (
            BitArrayStrategy,
            "TabuSearch",
            tabu_strat,
            3,
        )
    )

    for s1, s2 in itertools.product(strategies, repeat=2):
        strat1, s1name, *_ = s1
        strat2, s2name, *_ = s2
        match = Match(strat1, strat2, rounds)

        if isinstance(match.p1, BitArrayStrategy):
            match.p1.__name__ = s1[1]
            match.p1.set_params(s1[2], s1[3])

        if isinstance(match.p2, BitArrayStrategy):
            match.p2.__name__ = s2[1]
            match.p2.set_params(s2[2], s2[3])

        match.simulate()

        score1, score2 = match.p1.score / rounds, match.p2.score / rounds

        results[(s1name, s2name)] = (score1, score2)

    return results


# %%
def table(results):
    strategies = set()
    for strat1, strat2 in results.keys():
        strategies.add(strat1)
        strategies.add(strat2)

    strategies = sorted(strategies)
    data = {strat: {s: 0 for s in strategies} for strat in strategies}

    for (strat1, strat2), (_, score2) in results.items():
        data[strat1][strat2] = score2

    frame = pd.DataFrame(data)
    frame["Avg"] = frame.mean(axis=1)

    # Sorting by avg
    frame = frame.sort_values(by="Avg", ascending=False)

    frame = frame.round(2)
    print(frame)

    fig, ax = plot.subplots()
    ax.axis("tight")
    ax.axis("off")
    table = ax.table(
        cellText=frame.values,
        colLabels=frame.columns,
        rowLabels=frame.index,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    table.auto_set_column_width(col=list(range(len(frame.columns))))
    plot.show()

    return frame


# %%
def heatmap(frame):
    sns.heatmap(frame, annot=True, cmap="coolwarm", cbar=True)
    plot.show()


# %%
if __name__ == "__main__":
    from Strategy import (
        AlwaysCooperate,
        AlwaysDefect,
        TitForTat,
        TitFor2Tat,
        SuspiciousTitForTat,
        Random,
        GenerousTitForTat,
        Pavlov,
        GrimTrigger,
        Prober,
    )

    strategies = [
        AlwaysCooperate,
        AlwaysDefect,
        TitForTat,
        TitFor2Tat,
        SuspiciousTitForTat,
        Random,
        GenerousTitForTat,
        Pavlov,
        GrimTrigger,
        Prober,
    ]

    results = tournament(strategies)
    frame = table(results)
    heatmap(frame)

# %%
