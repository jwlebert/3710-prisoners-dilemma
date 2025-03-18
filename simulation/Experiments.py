from algorithms.GeneticAlgorithm import GeneticAlgorithm
from algorithms.HillClimbing import HillClimbing
from OptimizationAlgorithm import OptimizedTournament
import matplotlib.pyplot as plt
import pandas as pd
import time
import logging

logging.basicConfig(filename="experiment_logs.txt", level=logging.INFO, force=True)


def GeneticExperiments(pop_size, mutation_rate, memory_depth, generations):
    rounds = 100
    ga = GeneticAlgorithm(
        pop_size=pop_size, mutation_rate=mutation_rate, memory_depth=memory_depth
    )
    ga.train(generations=generations, rounds=rounds)
    genetic_strategy = ga.best_strategy()
    return (
        genetic_strategy,
        OptimizedTournament(genetic_strategy, memory_depth, rounds).get_score(),
    )


def HillClimbingExperiments(memory_depth, generations):
    rounds = 100
    hc = HillClimbing(memory_depth=memory_depth, rounds=rounds)
    hc.train(generations=generations, rounds=rounds)
    hill_climbing_strategy = hc.best_strategy()
    return (
        hill_climbing_strategy,
        OptimizedTournament(hill_climbing_strategy, memory_depth, rounds).get_score(),
    )


# %%


def create_table(df, title):
    fig, ax = plt.subplots()
    ax.axis("tight")
    ax.axis("off")
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    table.auto_set_column_width(col=list(range(len(df.columns))))

    # Add title above the table
    plt.figtext(0.5, 0.85, title, ha="center", fontsize=14)

    plt.tight_layout()

    plt.show()


def run_experiments(
    experiment_func, param_name, param_values, fixed_params, num_iterations, title
):
    param_results = []
    for value in param_values:
        params = fixed_params.copy()
        params[param_name] = value
        iteration_scores = []
        iteration_times = []

        for _ in range(num_iterations):
            iteration_start_time = time.time()

            strategy, score = experiment_func(**params)
            iteration_scores.append(score)

            iteration_end_time = time.time()
            iteration_time = iteration_end_time - iteration_start_time
            iteration_times.append(iteration_time)
            logging.info(
                f"Iteration time: {iteration_time:.2f} seconds, {param_name}: {value}, score: {score}"
            )

        avg_score = sum(iteration_scores) / num_iterations
        avg_time = sum(iteration_times) / num_iterations
        o = {
            param_name: value,
            "avg_time": round(avg_time, 2),
            "avg_score": round(avg_score, 2),
        }
        param_results.append(o)

    df = pd.DataFrame(param_results)
    df = df.sort_values(by="avg_score", ascending=False)
    logging.info(f"Results for {param_name}:")
    logging.info(df)

    create_table(df, title)

    return df


def run_genetic_experiments():
    results = []
    pop_sizes = [10, 20]
    mutation_rates = [0.01, 0.001]
    memory_depths = [3, 4]
    generations = [10, 20]
    num_iterations = 5  # Number of times to run each iteration

    fixed_params = {
        "pop_size": 10,
        "mutation_rate": 0.01,
        "memory_depth": 3,
        "generations": 10,
    }

    results.append(
        run_experiments(
            GeneticExperiments,
            "pop_size",
            pop_sizes,
            fixed_params,
            num_iterations,
            "Genetic Algorithm - Population Size",
        )
    )
    results.append(
        run_experiments(
            GeneticExperiments,
            "mutation_rate",
            mutation_rates,
            fixed_params,
            num_iterations,
            "Genetic Algorithm - Mutation Rate",
        )
    )

    results.append(
        run_experiments(
            GeneticExperiments,
            "memory_depth",
            memory_depths,
            fixed_params,
            num_iterations,
            "Genetic Algorithm - Memory Depth",
        )
    )
    results.append(
        run_experiments(
            GeneticExperiments,
            "generations",
            generations,
            fixed_params,
            num_iterations,
            "Genetic Algorithm - Generations",
        )
    )

    return results


def run_hill_climbing_experiments():
    results = []
    memory_depths = [3, 4]
    generations = [10, 20]
    num_iterations = 5  # Number of times to run each iteration

    fixed_params = {
        "memory_depth": 3,
        "generations": 10,
    }

    results.append(
        run_experiments(
            HillClimbingExperiments,
            "memory_depth",
            memory_depths,
            fixed_params,
            num_iterations,
            "Hill Climbing - Memory Depth",
        )
    )
    results.append(
        run_experiments(
            HillClimbingExperiments,
            "generations",
            generations,
            fixed_params,
            num_iterations,
            "Hill Climbing - Generations",
        )
    )

    return results


# %%
def main():
    run_genetic_experiments()
    run_hill_climbing_experiments()


# %%
if __name__ == "__main__":
    main()
# %%
