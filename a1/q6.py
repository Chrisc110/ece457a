import argparse

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

def check_valid_inputs(start, goal):
    start_x, start_y = start
    goal_x, goal_y = goal

    if start_x > MAX_X or start_y > MAX_Y:
        print("Starting coordinates out of bounds! Exiting...")
        return False
    
    if MAZE[start_x][start_y] == 1:
        print("Starting coordinates land on a wall! Exiting...")
        return False
    
    if goal_x > MAX_X or goal_y > MAX_Y:
        print("Goal coordinates out of bounds! Exiting...")
        return False
    
    if MAZE[goal_x][goal_y] == 1:
        print("Goal coordinates land on a wall! Exiting...")
        return False
    
    return True

def check_valid_move(node):
    x,y = node

    OPEN_SPACE = 0

    return x <= MAX_X and x >=0 and y <= MAX_Y and y >=0 and MAZE[x][y] == OPEN_SPACE;
    

def bfs(start, goal):
    visited = set()
    queue = [(0, start, [start])]

    while queue:

        cost, cur_node, path = queue.pop(0)

        if cur_node == goal:
            print(f"\nPath found: {path} with total cost: {cost}")
            return cost, path
        
        if cur_node not in visited:
            visited.add(cur_node)

            cur_x, cur_y = cur_node

            #Add up
            if (check_valid_move((cur_x, cur_y + 1))):
                queue.append((cost+1, (cur_x, cur_y + 1), path + [cur_node]))

            #Add down
            if (check_valid_move((cur_x, cur_y - 1))):
                queue.append((cost+1, (cur_x, cur_y - 1), path + [cur_node]))

            #Add left
            if (check_valid_move((cur_x - 1, cur_y))):
                queue.append((cost+1, (cur_x - 1, cur_y), path + [cur_node]))


            #add right
            if (check_valid_move((cur_x + 1, cur_y))):
                queue.append((cost+1, (cur_x + 1, cur_y), path + [cur_node]))

    print("Goal not found")

def dfs(start, goal):
    print()

def a_star(start, goal):
    print()

def add_path(path):
    for node in path:
        x,y = node

        MAZE[x][y] = '*'

def print_maze():
    for x in range (0,25):
        for y in range (0,25):
            print(f'{MAZE[x][y]} ', end="")
        
        print()


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
            print("Starting BFS search...")
            cost, path = bfs(start, goal)

        elif args.dfs:
            print("Starting DFS search...")
            dfs(start, goal)

        elif args.astar:
            print("Starting A Star search...")
            a_star(start, goal)
            
        else:
            print("Please select a search algorithm with -b (BFS), -d (DFS), or -a (A*).")

    add_path(path)
    print_maze()


if __name__ == "__main__":
    main()