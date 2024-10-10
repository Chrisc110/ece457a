import time
import random
import matplotlib.pyplot as plt


# Dummy data for flows and distances (you need to replace these with actual data)
FLOW_MATRIX = [[0.0, 0.0, 5.0, 0.0, 5.0, 2.0, 10.0, 3.0, 1.0, 5.0, 5.0, 5.0, 0.0, 0.0, 5.0, 4.0, 4.0, 0.0, 0.0, 1.0],
               [0.0, 0.0, 3.0, 10.0, 5.0, 1.0, 5.0, 1.0, 2.0, 4.0, 2.0, 5.0, 0.0, 10.0, 10.0, 3.0, 0.0, 5.0, 10.0, 5.0],
               [5.0, 3.0, 0.0, 2.0, 0.0, 5.0, 2.0, 4.0, 4.0, 5.0, 0.0, 0.0, 0.0, 5.0, 1.0, 0.0, 0.0, 5.0, 0.0, 0.0],
               [0.0, 10.0, 2.0, 0.0, 1.0, 0.0, 5.0, 2.0, 1.0, 0.0, 10.0, 2.0, 2.0, 0.0, 2.0, 1.0, 5.0, 2.0, 5.0, 5.0],
               [5.0, 5.0, 0.0, 1.0, 0.0, 5.0, 6.0, 5.0, 2.0, 5.0, 2.0, 0.0, 5.0, 1.0, 1.0, 1.0, 5.0, 2.0, 5.0, 1.0],
               [2.0, 1.0, 5.0, 0.0, 5.0, 0.0, 5.0, 2.0, 1.0, 6.0, 0.0, 0.0, 10.0, 0.0, 2.0, 0.0, 1.0, 0.0, 1.0, 5.0],
               [10.0, 5.0, 2.0, 5.0, 6.0, 5.0, 0.0, 0.0, 0.0, 0.0, 5.0, 10.0, 2.0, 2.0, 5.0, 1.0, 2.0, 1.0, 0.0, 10.0],
               [3.0, 1.0, 4.0, 2.0, 5.0, 2.0, 0.0, 0.0, 1.0, 1.0, 10.0, 10.0, 2.0, 0.0, 10.0, 2.0, 5.0, 2.0, 2.0, 10.0],
               [1.0, 2.0, 4.0, 1.0, 2.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 3.0, 5.0, 5.0, 0.0, 5.0, 0.0, 0.0, 0.0, 2.0],
               [5.0, 4.0, 5.0, 0.0, 5.0, 6.0, 0.0, 1.0, 2.0, 0.0, 5.0, 5.0, 0.0, 5.0, 1.0, 0.0, 0.0, 5.0, 5.0, 2.0],
               [5.0, 2.0, 0.0, 10.0, 2.0, 0.0, 5.0, 10.0, 0.0, 5.0, 0.0, 5.0, 2.0, 5.0, 1.0, 10.0, 0.0, 2.0, 2.0, 5.0],
               [5.0, 5.0, 0.0, 2.0, 0.0, 0.0, 10.0, 10.0, 3.0, 5.0, 5.0, 0.0, 2.0, 10.0, 5.0, 0.0, 1.0, 1.0, 2.0, 5.0],
               [0.0, 0.0, 0.0, 2.0, 5.0, 10.0, 2.0, 2.0, 5.0, 0.0, 2.0, 2.0, 0.0, 2.0, 2.0, 1.0, 0.0, 0.0, 0.0, 5.0],
               [0.0, 10.0, 5.0, 0.0, 1.0, 0.0, 2.0, 0.0, 5.0, 5.0, 5.0, 10.0, 2.0, 0.0, 5.0, 5.0, 1.0, 5.0, 5.0, 0.0],
               [5.0, 10.0, 1.0, 2.0, 1.0, 2.0, 5.0, 10.0, 0.0, 1.0, 1.0, 5.0, 2.0, 5.0, 0.0, 3.0, 0.0, 5.0, 10.0, 10.0],
               [4.0, 3.0, 0.0, 1.0, 1.0, 0.0, 1.0, 2.0, 5.0, 0.0, 10.0, 0.0, 1.0, 5.0, 3.0, 0.0, 0.0, 0.0, 2.0, 0.0],
               [4.0, 0.0, 0.0, 5.0, 5.0, 1.0, 2.0, 5.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 5.0, 2.0, 0.0],
               [0.0, 5.0, 5.0, 2.0, 2.0, 0.0, 1.0, 2.0, 0.0, 5.0, 2.0, 1.0, 0.0, 5.0, 5.0, 0.0, 5.0, 0.0, 1.0, 1.0],
               [0.0, 10.0, 0.0, 5.0, 5.0, 1.0, 0.0, 2.0, 0.0, 5.0, 2.0, 2.0, 0.0, 5.0, 10.0, 2.0, 2.0, 1.0, 0.0, 6.0],
               [1.0, 5.0, 0.0, 5.0, 1.0, 5.0, 10.0, 10.0, 2.0, 2.0, 5.0, 5.0, 5.0, 0.0, 10.0, 0.0, 0.0, 1.0, 6.0, 0.0]]

DISTANCE_MATRIX = [[0.0, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 4.0, 5.0, 6.0, 3.0, 4.0, 5.0, 6.0, 7.0],
                   [1.0, 0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 4.0, 5.0, 6.0],
                   [2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 4.0, 5.0],
                   [3.0, 2.0, 1.0, 0.0, 1.0, 4.0, 3.0, 2.0, 1.0, 2.0, 5.0, 4.0, 3.0, 2.0, 3.0, 6.0, 5.0, 4.0, 3.0, 4.0],
                   [4.0, 3.0, 2.0, 1.0, 0.0, 5.0, 4.0, 3.0, 2.0, 1.0, 6.0, 5.0, 4.0, 3.0, 2.0, 7.0, 6.0, 5.0, 4.0, 3.0],
                   [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                   [2.0, 1.0, 2.0, 3.0, 4.0, 1.0, 0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 3.0, 4.0, 5.0],
                   [3.0, 2.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 3.0, 4.0],
                   [4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0, 4.0, 3.0, 2.0, 1.0, 2.0, 5.0, 4.0, 3.0, 2.0, 3.0],
                   [5.0, 4.0, 3.0, 2.0, 1.0, 4.0, 3.0, 2.0, 1.0, 0.0, 5.0, 4.0, 3.0, 2.0, 1.0, 6.0, 5.0, 4.0, 3.0, 2.0],
                   [2.0, 3.0, 4.0, 5.0, 6.0, 1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0, 5.0],
                   [3.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0, 2.0, 3.0, 4.0, 1.0, 0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0],
                   [4.0, 3.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 2.0, 3.0],
                   [5.0, 4.0, 3.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0, 4.0, 3.0, 2.0, 1.0, 2.0],
                   [6.0, 5.0, 4.0, 3.0, 2.0, 5.0, 4.0, 3.0, 2.0, 1.0, 4.0, 3.0, 2.0, 1.0, 0.0, 5.0, 4.0, 3.0, 2.0, 1.0],
                   [3.0, 4.0, 5.0, 6.0, 7.0, 2.0, 3.0, 4.0, 5.0, 6.0, 1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 1.0, 2.0, 3.0, 4.0],
                   [4.0, 3.0, 4.0, 5.0, 6.0, 3.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.0, 2.0, 3.0, 4.0, 1.0, 0.0, 1.0, 2.0, 3.0],
                   [5.0, 4.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0],
                   [6.0, 5.0, 4.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0],
                   [7.0, 6.0, 5.0, 4.0, 3.0, 6.0, 5.0, 4.0, 3.0, 2.0, 5.0, 4.0, 3.0, 2.0, 1.0, 4.0, 3.0, 2.0, 1.0, 0.0]]

SOL_SIZE = 20
MAX_ITERATIONS = 200

# Function to calculate cost based on flow and distance
def calculate_cost(permutation):
    cost = 0
    for i in range(SOL_SIZE):
        for j in range(SOL_SIZE):
            cost += FLOW_MATRIX[permutation[i]][permutation[j]] * DISTANCE_MATRIX[i][j]
    return cost

# Tabu Search Algorithm
def tabu_search():
    best_solution = list(range(SOL_SIZE))
    best_cost = calculate_cost(best_solution)
    random.shuffle(best_solution)
    current_solution = best_solution[:]
    current_cost = best_cost

    tabu_list = []

    TABU_TENURE = 10
    
    for iteration in range(MAX_ITERATIONS):

        neighborhood = []
        
        # Generate neighborhood by swapping elements
        for i in range(SOL_SIZE):
            for j in range(i + 1, SOL_SIZE):
                neighbor = current_solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighborhood.append(neighbor)

        # Filter out tabu solutions
        neighborhood = [sol for sol in neighborhood if sol not in tabu_list]

        # If neighborhood is empty, break
        if not neighborhood:
            break

        # Evaluate neighborhood
        costs = [calculate_cost(neighbor) for neighbor in neighborhood]
        best_neighbor_index = costs.index(min(costs))
        best_neighbor = neighborhood[best_neighbor_index]
        best_neighbor_cost = costs[best_neighbor_index]

        # Update current solution if found a better solution
        if best_neighbor_cost < current_cost:
            current_solution = best_neighbor
            current_cost = best_neighbor_cost

        # Update best solution if found a new best
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        # Update tabu list
        tabu_list.append(current_solution)
        while (len(tabu_list) > TABU_TENURE):
            tabu_list.pop(0)

        if iteration % 20 == 0:
            TABU_TENURE += 2

    return (best_solution, best_cost)






# Execute Tabu Search
start_time = time.time()

# best_solution, best_cost = tabu_search()
# print("Best solution:", best_solution)
# print("Best cost:", best_cost)

costs = []
for i in range(20):
    solution, cost = tabu_search()
    costs.append(cost)

print(f"Lowest Cost: {min(costs)}")

# Iteration numbers from 1 to 20
iterations = list(range(1, len(costs) + 1))

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(iterations, costs, marker='o', linestyle='-', color='b')
plt.title('Cost vs Iteration Number')
plt.xlabel('Iteration Number')
plt.ylabel('Cost')
plt.xticks(iterations)  # Set x-axis ticks to increment by 1
plt.grid(True)
plt.show()



end_time = time.time()
exe_time = (end_time - start_time) * 1000
print(f"EXE TIME: {exe_time:.8f} ms")