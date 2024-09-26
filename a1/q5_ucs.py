import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue to store (cost, node, path)
    prio_queue = [(0, start, [start])]
    # Set to track visited nodes (closed set)
    visited = []
    iteration = 0  # Track iteration number

    while prio_queue:
        print(f"Open: {[[node, cost] for cost, node, path in prio_queue]}")
        print(f"Closed: {visited}")
        print()

        # Pop the node with the lowest cost from the queue
        (cost, current_node, path) = heapq.heappop(prio_queue)

        # If we've reached the goal, return the cost and the path
        if current_node == goal:
            print(f"\nPath found: {path} with total cost: {cost}")
            return cost, path

        # If the node has not been visited, expand it
        if current_node not in visited:
            visited.append(current_node)

            # Explore the neighbors of the current node
            for neighbor, travel_cost in graph[current_node]:
                if neighbor not in visited:
                    # Add neighbor to the queue with the updated cost and path
                    heapq.heappush(prio_queue, (cost + travel_cost, neighbor, path + [neighbor]))

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

# Run UCS from city 1 to city 7
cost, path = uniform_cost_search(graph, 1, 7)