import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools

# eval function
def sphere_function(individual):
    return sum(x**2 for x in individual),

# init deap
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimization
creator.create("Individual", list, fitness=creator.FitnessMin)

# init parameters
toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, -5.12, 5.12)  # Initialize within bounds
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, N=10)
toolbox.register("evaluate", sphere_function)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1.0/1200.0, indpb=1.0)

N = 10 
X_MIN, X_MAX = -5.12, 5.12
sigma = 1.0 / 1200.0 
C = 0.6  
G = 20  
MAX_GENERATIONS = 500  
NUM_SIMULATIONS = 50  

cost = [[] for _ in range(MAX_GENERATIONS)]

# run 50 simulations
for simulation in range(NUM_SIMULATIONS):
    individual = toolbox.individual()
    individual.fitness.values = toolbox.evaluate(individual)
    best_individual = individual
    best_cost = individual.fitness.values[0]
    successful_mutations = 0

    # iteration through generations
    for generation in range(MAX_GENERATIONS):
        
        # random values for mutation
        mutant = toolbox.clone(best_individual)
        toolbox.mutate(mutant, sigma=sigma)
        del mutant.fitness.values  

        # assert bounds
        for i in range(N):
            mutant[i] = np.clip(mutant[i], X_MIN, X_MAX)

        mutant.fitness.values = toolbox.evaluate(mutant)

        # check if child is better than parent
        if mutant.fitness.values[0] < best_cost:
            best_individual = mutant
            best_cost = mutant.fitness.values[0]
            successful_mutations += 1

        #update sigma
        if (generation + 1) % G == 0:
            phi = successful_mutations / G
            if phi < 1 / 5:
                sigma *= C ** 2
            elif phi > 1 / 5:
                sigma /= C ** 2
            successful_mutations = 0

        # store current best cost
        cost[generation].append(best_cost)

# average the costs across the simulations for each generation
avg_cost = [sum(gen_cost) / len(gen_cost) for gen_cost in cost]

# plot
generations = list(range(len(avg_cost)))
plt.plot(generations, avg_cost)
plt.xlabel('Generation')
plt.ylabel('Average Cost')
plt.title("Average Cost vs Generation Number over 50 Simulations")
plt.show()