from algorithms.GeneticAlgorithm import GeneticAlgorithm
from algorithms.HillClimbing import HillClimbing
from OptimizationAlgorithm import OptimizedTournament
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import time
import logging

from multiprocessing import Pool
import os


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


def create_parameter_graphs(df, param_name, title):
    # Create a single figure
    plt.figure(figsize=(10, 6))

    # Convert parameter values to strings for consistent color mapping
    df[param_name] = df[param_name].astype(str)

    # Explode the scores list into separate rows
    plot_df = df.explode("scores")
    plot_df["scores"] = plot_df["scores"].astype(float)

    # Calculate average scores for each parameter value
    avg_scores = plot_df.groupby(param_name)["scores"].mean()

    # Create the boxplot with updated syntax
    sns.boxplot(
        data=plot_df,
        x=param_name,
        y="scores",
        hue=param_name,  # Add hue parameter
        width=0.5,
        saturation=0.7,
        legend=False,  # Hide redundant legend
    )

    # Add individual points
    sns.swarmplot(
        x=param_name,
        y="scores",
        data=plot_df,
        size=8,
        color="black",
        alpha=0.6,
        edgecolor="white",
        linewidth=0.5,
    )

    # Add average score labels
    ax = plt.gca()
    for i, avg in enumerate(avg_scores):
        ax.text(
            i,
            ax.get_ylim()[1],
            f"Avg: {avg:.2f}",
            horizontalalignment="center",
            verticalalignment="bottom",
        )

    # Customize the plot
    plt.title(f"Scores Distribution by {param_name}", pad=20, fontsize=12)
    plt.ylabel("Score")
    plt.xlabel(param_name)
    plt.grid(True, alpha=0.2)
    plt.xticks(rotation=45)

    # Add main title with padding
    plt.suptitle(title, fontsize=14, y=1.05)

    # Adjust layout
    plt.tight_layout()
    plt.show()


def run_single_experiment(params):
    """Helper function to run a single experiment iteration"""
    experiment_func = params["experiment_func"]
    func_params = params["func_params"]

    iteration_start_time = time.time()
    strategy, score = experiment_func(**func_params)
    iteration_end_time = time.time()

    return {"score": score, "time": iteration_end_time - iteration_start_time}


def run_experiments(
    experiment_func, param_name, param_values, fixed_params, num_iterations, title
):
    param_results = []
    detailed_results = []

    for value in param_values:
        params = fixed_params.copy()
        params[param_name] = value

        # Prepare parameters for parallel processing
        experiment_params = [
            {"experiment_func": experiment_func, "func_params": params}
            for _ in range(num_iterations)
        ]

        # Use number of CPU cores minus 1 to avoid overloading
        num_processes = max(1, os.cpu_count() - 1)

        # Run experiments in parallel
        with Pool(processes=num_processes) as pool:
            iteration_results = pool.map(run_single_experiment, experiment_params)

        # Store all scores and times
        scores = [result["score"] for result in iteration_results]
        times = [result["time"] for result in iteration_results]

        # Calculate averages
        avg_score = (
            sum(result["score"] for result in iteration_results) / num_iterations
        )
        avg_time = sum(result["time"] for result in iteration_results) / num_iterations

        # Store summarized results for the table
        param_results.append(
            {
                param_name: value,
                "avg_time": round(avg_time, 2),
                "avg_score": round(avg_score, 2),
            }
        )
        # Store detailed results for the graphs
        detailed_results.append(
            {
                param_name: value,
                "scores": scores,
                "times": times,
            }
        )

        logging.info(
            f"Completed {num_iterations} iterations for {param_name}: {value}, "
            f"avg_score: {avg_score:.2f}, avg_time: {avg_time:.2f}"
        )

    # Create summary DataFrame for tables
    summary_df = pd.DataFrame(param_results)
    summary_df = summary_df.sort_values(by="avg_score", ascending=False)

    # Create detailed DataFrame for graphs
    detailed_df = pd.DataFrame(detailed_results)

    logging.info(f"Results for {param_name}:")
    logging.info(summary_df)

    # Create table with averages
    create_table(summary_df, f"{title} - Table")
    # Create graphs with individual points
    create_parameter_graphs(detailed_df, param_name, title)

    return summary_df


def run_genetic_experiments():
    results = []
    pop_sizes = [20, 10]
    mutation_rates = [0.01, 0.05]
    memory_depths = [3, 4]
    generations = [10, 20, 30]
    num_iterations = 5  # Number of times to run each iteration

    fixed_params = {
        "pop_size": 20,
        "mutation_rate": 0.01,
        "memory_depth": 3,
        "generations": 20,
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
    generations = [100, 50]
    num_iterations = 10  # Number of times to run each iteration

    fixed_params = {
        "memory_depth": 3,
        "generations": 100,
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
    print("Running Genetic Algorithm Experiments...")
    genetic_results = run_genetic_experiments()

    print("\nRunning Hill Climbing Experiments...")
    hillclimbing_results = run_hill_climbing_experiments()

    # Save results to CSV files
    results_dir = "experiment_results"
    os.makedirs(results_dir, exist_ok=True)

    for i, df in enumerate(genetic_results):
        df.to_csv(f"{results_dir}/genetic_experiment_{i+1}.csv", index=False)

    for i, df in enumerate(hillclimbing_results):
        df.to_csv(f"{results_dir}/hillclimbing_experiment_{i+1}.csv", index=False)


# %%
if __name__ == "__main__":
    main()
# %%
