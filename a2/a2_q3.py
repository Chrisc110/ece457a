import time
import random
import matplotlib.pyplot as plt
import numpy as np

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
PENALTY_WEIGHT = 0.25
TABU_TENURE = 20
MAX_NO_IMPROVEMENT = 10

# Function to calculate cost based on flow and distance
def calculate_cost(permutation):
    cost = 0
    for i in range(SOL_SIZE):
        for j in range(SOL_SIZE):
            cost += FLOW_MATRIX[permutation[i]][permutation[j]] * DISTANCE_MATRIX[i][j]
    return cost

def tabu_search():
    best_solution = list(range(SOL_SIZE))
    random.shuffle(best_solution)
    best_cost = calculate_cost(best_solution)

    current_solution = best_solution[:]
    current_cost = best_cost

    tabu_list = []
    move_frequency = np.zeros((SOL_SIZE, SOL_SIZE))  # Frequency matrix to track how often moves are used

    no_improvement = 0

    for iteration in range(MAX_ITERATIONS):
        neighborhood = []
        moves = []
        
        # Create neighborhood
        for i in range(SOL_SIZE):
            for j in range(i + 1, SOL_SIZE):
                neighbor = current_solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighborhood.append(neighbor)
                moves.append((i, j))

        best_neighbor = None
        best_neighbor_cost = float('inf')
        best_move = None

        for idx, neighbor in enumerate(neighborhood):
            neighbor_cost = calculate_cost(neighbor)
            move = moves[idx]

            # Add penalty to frequency visited moves
            penalty = PENALTY_WEIGHT * move_frequency[move[0], move[1]]
            neighbor_cost += penalty

            # Check if move is in tabu list
            if move in tabu_list:
                if neighbor_cost < best_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost
                    best_move = move
                    break
            else:
                if neighbor_cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost
                    best_move = move

        if best_neighbor is None:
            break

        current_solution = best_neighbor
        current_cost = best_neighbor_cost

        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
            no_improvement = 0

        else:
            no_improvement += 1

        if no_improvement >= MAX_NO_IMPROVEMENT:
            current_solution = list(range(SOL_SIZE))
            random.shuffle(current_solution)
            current_cost = calculate_cost(current_solution)
            tabu_list.clear()  # Optionally clear tabu list
            no_improvement = 0  # Reset stagnation counter
            move_frequency = np.zeros((SOL_SIZE, SOL_SIZE))

        # Update tabu list with the move
        tabu_list.append(best_move)
        if len(tabu_list) > TABU_TENURE:
            tabu_list.pop(0)

        # Update move frequency
        move_frequency[best_move[0], best_move[1]] += 1

    return (best_solution, best_cost)

# Keep track of execution time
start_time = time.time()

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