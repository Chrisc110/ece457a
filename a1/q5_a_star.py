import heapq

def a_star_search(graph, start, goal, heuristics):
    # Priority queue to store (total_cost, g(n), node, path)
    prio_queue = [(heuristics[start], 0, start, [start])]
    # Set to track visited nodes (closed set)
    visited = []
    
    # Print header
    iteration = 0  # Track iteration number

    while prio_queue:

        print(f"Open: {[[current_node, f_cost] for f_cost, g_node, current_node, path in prio_queue]}")
        print(f"Closed: {visited}")
        print()

        # Pop the node with the lowest total cost (f(n) = g(n) + h(n)) from the queue
        (f_cost, g_cost, current_node, path) = heapq.heappop(prio_queue)

        # If we've reached the goal, return the total cost and the path
        if current_node == goal:
            print(f"\nPath found: {path} with total cost: {g_cost}")
            return g_cost, path

        # If the node has not been visited, expand it
        if current_node not in visited:
            visited.append(current_node)

            # Explore the neighbors of the current node
            for neighbor, travel_cost in graph[current_node]:
                if neighbor not in visited:
                    # Calculate g(n) (cost to reach the neighbor)
                    new_g_cost = g_cost + travel_cost
                    # Calculate f(n) = g(n) + h(n)
                    new_f_cost = new_g_cost + heuristics[neighbor]
                    # Add the neighbor to the priority queue
                    heapq.heappush(prio_queue, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))

        iteration += 1  # Increment iteration count

    # If goal is not reachable, return None
    print("No path found.")
    return None

# Define the graph as an adjacency list with (neighbor, cost)
graph = {
    1: [(5, 5), (8, 24)],
    5: [(1, 5), (6, 35)],
    8: [(1, 24), (3, 23), (10, 15)],
    3: [(8, 23), (4, 7), (10, 24)],
    4: [(3, 7), (9, 18)],
    9: [(4, 18), (10, 26), (6, 26), (7, 35), (2, 35)],
    10: [(3, 24), (9, 26), (6, 30), (8, 15)],
    6: [(5, 35), (9, 26), (10, 30), (2, 38)],
    2: [(6, 38), (7, 32), (9, 35)],
    7: [(9, 35), (2, 32)]
}
# Define the heuristic (h(n)) values as shown in the red boxes (distance estimate to city 7)
heuristics = {
    1: 78,
    2: 32,
    3: 37,
    4: 30,
    5: 75,
    6: 60,
    7: 0,  # The heuristic for the goal node is always 0
    8: 60,
    9: 35,
    10: 57
}

# Run A* from city 1 to city 7
cost, path = a_star_search(graph, 1, 7, heuristics)