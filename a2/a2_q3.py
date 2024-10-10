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
MAX_NO_IMPROVEMENT = 10

# Function to calculate cost based on flow and distance
def calculate_cost(permutation):
    cost = 0
    for i in range(SOL_SIZE):
        for j in range(SOL_SIZE):
            cost += FLOW_MATRIX[permutation[i]][permutation[j]] * DISTANCE_MATRIX[i][j]
    return cost

# Tabu Search Algorithm
def tabu_search():
    TABU_TENURE = 20

    best_solution = list(range(SOL_SIZE))
    random.shuffle(best_solution)
    best_cost = calculate_cost(best_solution)

    current_solution = best_solution[:]
    current_cost = best_cost

    tabu_list = []

    no_improvement = 0

    for iteration in range(MAX_ITERATIONS):
        neighborhood = []
        moves = []
        
        # Generate neighborhood by swapping elements
        for i in range(SOL_SIZE):
            for j in range(i + 1, SOL_SIZE):
                neighbor = current_solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighborhood.append(neighbor)
                moves.append((i, j))  # Track the move (swap)

        # Evaluate neighborhood and track which moves are tabu
        best_neighbor = None
        best_neighbor_cost = float('inf')
        best_move = None

        for idx, neighbor in enumerate(neighborhood):
            neighbor_cost = calculate_cost(neighbor)
            move = moves[idx]
 
            # Check if move is tabu
            if move in tabu_list:
                # Apply aspiration criterion: allow if it improves the global best solution
                if neighbor_cost < best_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost
                    best_move = move
                    break  # Immediate move due to aspiration criterion
            else:
                # If not tabu and better than current best in neighborhood, select it
                if neighbor_cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost
                    best_move = move

        # If no valid moves, stop the search
        if best_neighbor is None:
            break

        # Update current solution and cost
        current_solution = best_neighbor
        current_cost = best_neighbor_cost

        # Update global best solution if necessary
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
            no_improvement = 0
        
        else:
            no_improvement += 1

        # Update tabu list with the move
        tabu_list.append(best_move)
        if len(tabu_list) > TABU_TENURE:
            tabu_list.pop(0)

        if no_improvement >= MAX_NO_IMPROVEMENT:
            current_solution = list(range(SOL_SIZE))
            random.shuffle(current_solution)
            current_cost = calculate_cost(current_solution)
            tabu_list.clear()  # Optionally clear tabu list
            no_improvement = 0  # Reset stagnation counter

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