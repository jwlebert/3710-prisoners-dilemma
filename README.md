# 3710-prisoners-dilemma
# Iterated Prisoner's Dilemma

Optimization methods for the Iterated Prisoner's Dilemma using genetic algorithms, hill climbing, and tabu search.

**COMP-3710 Project - University of Windsor**  
Authors: Joshua Lebert, Julia Ducharme, Norika Upadhyay, Tansh Koul

📄 **[Read the full paper](./Exploration%20of%20the%20Iterated%20Prisoner's%20Dilemma.pdf)**

## Overview

This project explores different strategies for the Iterated Prisoner's Dilemma (IPD) and compares optimization methods to evolve effective strategies. Players repeatedly choose to cooperate or defect, with decisions based on previous game history.

## Key Findings

- **Memory depth of 2** yielded the highest average scores
- **Genetic algorithms** performed best overall
- **Population size of 250** and **250 generations** were optimal for GA
- Successful strategies are nice, provocable, and forgiving

## Implemented Strategies

**Human Strategies**: Always Cooperate, Always Defect, Tit-for-Tat, Suspicious Tit-for-Tat, Tit-for-2-Tat, Generous Tit-for-Tat, Pavlov, Grim Trigger, Random

**Optimization Methods**: Genetic Algorithm, Hill Climbing, Hill Climbing with Random Restart, Tabu Search

## Usage

```bash
git clone https://github.com/jwlebert/3710-prisoners-dilemma.git
cd 3710-prisoners-dilemma
pip install -r requirements.txt
```

Run experiments:
```bash
python genetic_algorithm.py --generations 250 --population 250 --memory_depth 2
python hill_climbing.py --iterations 10 --memory_depth 2
python tabu_search.py --iterations 250 --memory_depth 2
```

## Contributors

- **Joshua Lebert**: Optimization methods implementation
- **Julia Ducharme**: Experimentation and data analysis  
- **Norika Upadhyay**: Documentation
- **Tansh Koul**: Literature review
