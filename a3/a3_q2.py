import numpy as np
import matplotlib.pyplot as plt

# eval function
def sphere_function(x):
    return np.sum(x ** 2)

# init parameters
N = 10
X_MIN, X_MAX = -5.12, 5.12
sigma = 1.0/1200.0 
C = 0.6
G = 20
MAX_GENERATIONS = 500
NUM_SIMULATIONS = 50

# inital value/guess
x0 = np.random.uniform(X_MIN, X_MAX, N)
best_cost = sphere_function(x0)
successful_mutations = 0
cost = [[] for x in range(MAX_GENERATIONS)]

# run 50 simulations
for simulation in range(NUM_SIMULATIONS):
    #iteration through generations
    for generation in range(MAX_GENERATIONS):

        # random values for mutation
        r = np.random.normal(0, sigma, N)
        x1 = x0 + r

        # assert bounds
        x1 = np.clip(x1, X_MIN, X_MAX)

        # evaluate child
        f_x1 = sphere_function(x1)
        
        # check if child is better than parent
        if f_x1 < best_cost:
            x0 = x1
            best_cost = f_x1
            successful_mutations += 1
        
        # udpate sigma
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
plt.xlabel('Generation number')
plt.ylabel('Average Cost')
plt.title("Average Cost vs Generation Number over 50 iterations")
plt.show()