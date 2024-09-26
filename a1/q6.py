import argparse
import heapq

MAZE = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #25 (Bottom Row)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], # 20 
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0], # 15
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], # 5
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]] # 1 (Top Row)

def parse_coordinates(coord_str):
    """ Helper function to parse a coordinate string like 'x,y' """
    x, y = map(int, coord_str.split(','))
    return (x, y)


MAX_X = 24
MAX_Y = 24

# Check start and goal coordinates for conflicts
def check_valid_inputs(start, goal):
    start_x, start_y = start
    goal_x, goal_y = goal

    if start_x > MAX_X or start_y > MAX_Y:
        print("Starting coordinates out of bounds! Exiting...")
        return False
    
    if MAZE[start_y][start_x] == 1:
        print("Starting coordinates land on a wall! Exiting...")
        return False
    
    if goal_x > MAX_X or goal_y > MAX_Y:
        print("Goal coordinates out of bounds! Exiting...")
        return False
    
    if MAZE[goal_y][goal_x] == 1:
        print("Goal coordinates land on a wall! Exiting...")
        return False
    
    return True

# Check if a move to a specific node if valid
def check_valid_move(node):
    x,y = node

    OPEN_SPACE = 0

    return x <= MAX_X and x >=0 and y <= MAX_Y and y >=0 and MAZE[y][x] == OPEN_SPACE
    
# Convert a node in the path to a star in the array holding the maze
def add_path(path):
    for node in path:
        x,y = node

        MAZE[y][x] = '*'

# Print the maze in a human readable format
def print_maze():
    for y in range (24, -1, -1):
        for x in range (0, 25):
            print(f'{MAZE[y][x]} ', end="")
        
        print()

# Implementation of BFS
def bfs(start, goal):
    visited = set()
    queue = [(0, start, [])]

    iteration = 0

    while queue:

        cost, cur_node, path = queue.pop(0)

        if cur_node == goal:
            path = path + [cur_node]
            cost = cost + 1
            print(f"Iterations: {iteration}")
            return cost, path
        
        if cur_node not in visited:
            visited.add(cur_node)

            cur_x, cur_y = cur_node

            if (check_valid_move((cur_x + 1, cur_y))):
                queue.append((cost+1, (cur_x + 1, cur_y), path + [cur_node]))

            if (check_valid_move((cur_x - 1, cur_y))):
                queue.append((cost+1, (cur_x - 1, cur_y), path + [cur_node]))

            if (check_valid_move((cur_x, cur_y + 1))):
                queue.append((cost+1, (cur_x, cur_y + 1), path + [cur_node]))

            if (check_valid_move((cur_x, cur_y - 1))):
                queue.append((cost+1, (cur_x, cur_y - 1), path + [cur_node]))

        iteration += 1

            

    print("Goal not found")

# Implementation of DFS
def dfs(start, goal):
    visited = set()
    queue = [(0, start, [])]

    iteration = 0

    while queue:

        cost, cur_node, path = queue.pop()

        if cur_node == goal:
            path = path + [cur_node]
            cost = cost + 1
            print(f"Iterations: {iteration}")
            return cost, path
        
        if cur_node not in visited:
            visited.add(cur_node)

            cur_x, cur_y = cur_node

            if (check_valid_move((cur_x + 1, cur_y))):
                queue.append((cost+1, (cur_x + 1, cur_y), path + [cur_node]))

            if (check_valid_move((cur_x - 1, cur_y))):
                queue.append((cost+1, (cur_x - 1, cur_y), path + [cur_node]))

            if (check_valid_move((cur_x, cur_y - 1))):
                queue.append((cost+1, (cur_x, cur_y - 1), path + [cur_node]))

            if (check_valid_move((cur_x, cur_y + 1))):
                queue.append((cost+1, (cur_x, cur_y + 1), path + [cur_node]))

        iteration += 1

    print("Goal not found")

# Implementation of a heuristics function for A* search
def h(cur_node, goal):
    cur_x, cur_y = cur_node
    goal_x, goal_y = goal

    # Implementation of Manhattan distance
    return abs(goal_x - cur_x) + abs(goal_y - cur_y)

# Implementation of A* search
def a_star(start, goal):
    # Priority queue to store (total_cost, g(n), node, path)
    prio_queue = [(h(start, goal), 0, start, [start])]
    # Set to track visited nodes (closed set)
    visited = set()
    
    # Print header
    iteration = 0  # Track iteration number

    while prio_queue:

        # Pop the node with the lowest total cost (f(n) = g(n) + h(n)) from the queue
        (f_cost, g_cost, current_node, path) = heapq.heappop(prio_queue)

        # If we've reached the goal, return the total cost and the path
        if current_node == goal:
            print(f"Iterations: {iteration}")
            return g_cost + 1, path

        # If the node has not been visited, expand it
        if current_node not in visited:
            visited.add(current_node)

            cur_x, cur_y = current_node

            TRAVEL_COST = 1
            if (check_valid_move((cur_x + 1, cur_y))):
                neighbor = (cur_x + 1, cur_y)
                # Calculate g(n) (cost to reach the neighbor)
                new_g_cost = g_cost + TRAVEL_COST
                # Calculate f(n) = g(n) + h(n)
                new_f_cost = new_g_cost + h(neighbor, goal)
                heapq.heappush(prio_queue, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))

            if (check_valid_move((cur_x - 1, cur_y))):
                neighbor = (cur_x - 1, cur_y)
                # Calculate g(n) (cost to reach the neighbor)
                new_g_cost = g_cost + TRAVEL_COST
                # Calculate f(n) = g(n) + h(n)
                new_f_cost = new_g_cost + h(neighbor, goal)
                heapq.heappush(prio_queue, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))

            if (check_valid_move((cur_x, cur_y + 1))):
                neighbor = (cur_x, cur_y + 1)
                # Calculate g(n) (cost to reach the neighbor)
                new_g_cost = g_cost + TRAVEL_COST
                # Calculate f(n) = g(n) + h(n)
                new_f_cost = new_g_cost + h(neighbor, goal)
                heapq.heappush(prio_queue, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))

            if (check_valid_move((cur_x, cur_y - 1))):
                neighbor = (cur_x, cur_y - 1)
                # Calculate g(n) (cost to reach the neighbor)
                new_g_cost = g_cost + TRAVEL_COST
                # Calculate f(n) = g(n) + h(n)
                new_f_cost = new_g_cost + h(neighbor, goal)
                heapq.heappush(prio_queue, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))


        iteration += 1  # Increment iteration count

    # If goal is not reachable, return None
    print("No path found.")
    return None


def main():
    parser = argparse.ArgumentParser(description="Search Algorithm Runner")
    
    parser.add_argument('-b', '--bfs', action='store_true', help="Run Breadth-First Search")
    parser.add_argument('-d', '--dfs', action='store_true', help="Run Depth-First Search")
    parser.add_argument('-a', '--astar', action='store_true', help="Run A* Search")
    parser.add_argument('start', type=parse_coordinates, help="Starting coordinate in 'x,y' format")
    parser.add_argument('goal', type=parse_coordinates, help="Goal coordinate in 'x,y' format")
    
    args = parser.parse_args()

    start = args.start
    goal = args.goal
    path = []

    if check_valid_inputs(start, goal):
        if args.bfs:
            print("Starting BFS search...\n")
            cost, path = bfs(start, goal)

        elif args.dfs:
            print("Starting DFS search...\n")
            cost, path = dfs(start, goal)

        elif args.astar:
            print("Starting A Star search...\n")
            cost, path = a_star(start, goal)
            
        else:
            print("Please select a search algorithm with -b (BFS), -d (DFS), or -a (A*).")

        print(f"Path found: {path}")
        print(f"Cost: {cost}")
        print()
        add_path(path)
        print_maze()

if __name__ == "__main__":
    main()