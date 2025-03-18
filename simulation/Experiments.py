from algorithms.GeneticAlgorithm import GeneticAlgorithm
from algorithms.HillClimbing import HillClimbing
from OptimizationAlgorithm import OptimizedTournament
import matplotlib.pyplot as plt
import pandas as pd
import time


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


def run_genetic_experiments():
    results = []
    pop_sizes = [10, 20]
    mutation_rates = [0.01, 0.001]
    memory_depths = [3, 4]
    generations = [10, 20]
    num_iterations = 5  # Number of times to run each iteration

    def test_parameter(parameter_name, parameter_values, fixed_params):
        param_results = []
        for value in parameter_values:
            params = fixed_params.copy()
            params[parameter_name] = value
            iteration_scores = []
            iteration_times = []

            for _ in range(num_iterations):
                iteration_start_time = time.time()

                genetic_strategy, genetic_score = GeneticExperiments(
                    params["pop_size"],
                    params["mutation_rate"],
                    params["memory_depth"],
                    params["generations"],
                )
                iteration_scores.append(genetic_score)

                iteration_end_time = time.time()
                iteration_time = iteration_end_time - iteration_start_time
                iteration_times.append(iteration_time)
                print(f"Iteration time: {iteration_time:.2f} seconds")

            avg_score = sum(iteration_scores) / num_iterations
            avg_time = sum(iteration_times) / num_iterations
            o = {
                parameter_name: value,
                "genetic_score": round(avg_score, 2),
                "avg_time": round(avg_time, 2),
            }
            param_results.append(o)

        df = pd.DataFrame(param_results)
        df = df.sort_values(by="genetic_score", ascending=False)
        print(f"Results for {parameter_name}:")
        print(df)

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
        plt.show()

        return df

    fixed_params = {
        "pop_size": 10,
        "mutation_rate": 0.01,
        "memory_depth": 3,
        "generations": 10,
    }

    test_parameter("pop_size", pop_sizes, fixed_params)
    test_parameter("mutation_rate", mutation_rates, fixed_params)
    test_parameter("memory_depth", memory_depths, fixed_params)
    test_parameter("generations", generations, fixed_params)

    return results


def run_hill_climbing_experiments():
    results = []
    memory_depths = [3, 4]
    generations = [10, 20]
    num_iterations = 5  # Number of times to run each iteration

    def test_parameter(parameter_name, parameter_values, fixed_params):
        param_results = []
        for value in parameter_values:
            params = fixed_params.copy()
            params[parameter_name] = value
            iteration_scores = []
            iteration_times = []

            for _ in range(num_iterations):
                iteration_start_time = time.time()

                hill_climbing_strategy, hill_climbing_score = HillClimbingExperiments(
                    params["memory_depth"], params["generations"]
                )
                iteration_scores.append(hill_climbing_score)

                iteration_end_time = time.time()
                iteration_time = iteration_end_time - iteration_start_time
                iteration_times.append(iteration_time)
                print(f"Iteration time: {iteration_time:.2f} seconds")

            avg_score = sum(iteration_scores) / num_iterations
            avg_time = sum(iteration_times) / num_iterations
            o = {
                parameter_name: value,
                "hill_climbing_score": round(avg_score, 2),
                "avg_time": round(avg_time, 2),
            }
            param_results.append(o)

        df = pd.DataFrame(param_results)
        df = df.sort_values(by="hill_climbing_score", ascending=False)
        print(f"Results for {parameter_name}:")
        print(df)

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
        plt.show()

        return df

    fixed_params = {
        "memory_depth": 3,
        "generations": 10,
    }

    test_parameter("memory_depth", memory_depths, fixed_params)
    test_parameter("generations", generations, fixed_params)

    return results


# %%
def main():
    run_genetic_experiments()
    run_hill_climbing_experiments()


# %%
if __name__ == "__main__":
    main()
# %%
