import heapq

# Define grid and start/goal positions
grid = [
    ['S', '.', '.', 'X', 'X'],
    ['.', 'X', '.', '.', '.'],
    ['.', 'X', 'X', '.', 'X'],
    ['.', '.', '.', '.', '.'],
    ['X', '.', 'X', 'X', 'G']
]

start = (0, 0)
goal = (4, 4)

# Define movement directions (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Define A* search function
def astar_search(grid, start, goal):
    def heuristic(node):
        # Calculate Manhattan distance as the heuristic
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_set = [(0, start)]  # Priority queue (f, node)
    came_from = {}  # Dictionary to store parent nodes
    g_score = {pos: float('inf') for row in grid for pos in row}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X':
                tentative_g_score = g_score[current] + 1
                if (tentative_g_score < g_score[(x, y)]):
                    came_from[(x, y)] = current
                    g_score[(x, y)] = tentative_g_score
                    f = tentative_g_score + heuristic((x, y))
                    heapq.heappush(open_set, (f, (x, y)))

    return None  # No path found

# Find and print the path
path = astar_search(grid, start, goal)
if path:
    print("Shortest Path:")
    for i in range(len(grid)):
        result = []
        for j in range (len(grid[0])):
            pos = (i, j)
            if pos == start:
                result.append('S')
            elif pos == goal:
                result.append('G')
            elif pos in path:
                result.append('*')
            else:
                result.append(grid[i][j])
        print(' '.join(result))
else:
    print("No path found.")