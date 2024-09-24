import heapq

def greedy_best_first_search(graph, start, goal):
    # Priority queue to store (cost, node, path)
    pq = [(0, start, [start])]
    # Set to track visited nodes (closed set)
    visited = []
    
    # Print header
    # print(f"{'Iteration':<10} {'Open Queue (cost, node, path)':<40} {'Closed Queue (visited nodes)'}")

    iteration = 0  # Track iteration number

    while pq:
        # print(pq)
        print(f"Open: {[[node, cost] for cost, node, path in pq]}")
        print(f"Closed: {visited}")
        print()

        # Print the current open queue and closed set
        # print(f"{iteration:<10} {[(c, n, p) for (c, n, p) in pq]:<40} {list(visited)}")

        # Pop the node with the lowest cost from the queue
        (cost, current_node, path) = heapq.heappop(pq)

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
                    heapq.heappush(pq, (travel_cost, neighbor, path + [neighbor]))

        iteration += 1  # Increment iteration count

    # If goal is not reachable, return None
    print("No path found.")
    return None

# Define the graph as an adjacency list with (neighbor, cost)
graph = {
    1: [(5, 75), (8, 60)],
    5: [(1, 78), (6, 60)],
    8: [(1, 78), (3, 37), (10, 57)],
    3: [(8, 60), (4,30), (10, 57)],
    4: [(3, 37), (9, 35)],
    9: [(4, 40), (10, 57), (6, 60), (7, 0), (2, 32)],
    10: [(3, 37), (9, 35), (6, 60), (8, 60)],
    6: [(5, 75), (9, 35), (10, 57), (2, 32)],
    2: [(6, 60), (7, 0), (9, 35)],
    7: [(9, 35), (2, 32)]
}

# Run UCS from city 1 to city 7
cost, path = greedy_best_first_search(graph, 1, 7)