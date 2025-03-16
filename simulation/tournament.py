# %%
import itertools
import matplotlib.pyplot as plot
import pandas as pd
import seaborn as sns

from Match import Match
from Strategy import (
    AlwaysCooperate,
    AlwaysDefect,
    TitForTat,
    TitFor2Tat,
    SuspiciousTitForTat,
    Random,
    GenerousTitForTat,
)

strategies = [
    AlwaysCooperate,
    AlwaysDefect,
    TitForTat,
    TitFor2Tat,
    SuspiciousTitForTat,
    Random,
    GenerousTitForTat,
]


def tournament(strategies, rounds=1000):
    results = {}

    for strat1, strat2 in itertools.product(strategies, repeat=2):
        match = Match(strat1, strat2, rounds)
        match.simulate()

        score1, score2 = match.p1.score / rounds, match.p2.score / rounds

        results[(strat1.__name__, strat2.__name__)] = (score1, score2)

    return results


# %%
def table(results):
    strategies = set()
    for strat1, strat2 in results.keys():
        strategies.add(strat1)
        strategies.add(strat2)

    strategies = sorted(strategies)
    data = {strat: {s: 0 for s in strategies} for strat in strategies}

    for (strat1, strat2), (score1, score2) in results.items():
        data[strat1][strat2] = score1
        data[strat1][strat2] = score2

    frame = pd.DataFrame(data)
    frame["Avg"] = frame.mean(axis=1)

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
    results = tournament(strategies)
    frame = table(results)
    heatmap(frame)

# %%
