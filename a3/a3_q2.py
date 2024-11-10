import numpy as np

# Define the sphere function
def sphere_function(x):
    return np.sum(x ** 2)

# Parameters
n = 10  # Dimension of the problem
x_min, x_max = -5.12, 5.12  # Boundaries of the search space
sigma = 1.0/1200.0  # Initial mutation variance
c = 0.817  # Control parameter for adaptive mutation
G = 20  # Window of generations for tracking success
max_generations = 500  # Termination after a set number of generations

# Initialize
x0 = np.random.uniform(x_min, x_max, n)
best_value = sphere_function(x0)
successful_mutations = 0
cost = []

# Evolution Strategy Loop
for generation in range(max_generations):
    # Generate a random mutation vector r from N(0, sigma^2)
    r = np.random.normal(0, sigma, n)
    x1 = x0 + r

    # Ensure x1 is within bounds
    x1 = np.clip(x1, x_min, x_max)

    # Evaluate the new candidate solution
    f_x1 = sphere_function(x1)
    
    # Selection: If the new solution is better, accept it
    if f_x1 < best_value:
        x0 = x1
        best_value = f_x1
        successful_mutations += 1
    
    # Adjust mutation variance sigma based on success rate over the past G generations
    if (generation + 1) % G == 0:
        phi = successful_mutations / G
        if phi < 1 / 5:
            sigma *= c ** 2
        elif phi > 1 / 5:
            sigma /= c ** 2
        # Reset the success count
        successful_mutations = 0

    cost.append(best_value)

# Result
print("Final solution:", x0)
print("Function value:", best_value)
print("Generations:", generation)
print("Cost: ", cost)