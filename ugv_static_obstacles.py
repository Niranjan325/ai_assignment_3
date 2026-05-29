import random
import heapq

GRID_SIZE = 20

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            neighbor = (current[0]+dx, current[1]+dy)

            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 0):

                temp_g = g_score[current] + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f_score = temp_g + heuristic(neighbor, goal)

                    heapq.heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current

    return None

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

density = 0.2

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if random.random() < density:
            grid[i][j] = 1

start = (0, 0)
goal = (19, 19)

grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

path = astar(grid, start, goal)

if path:
    print("Path Found")
    print("Path Length:", len(path))
    print(path)
else:
    print("No Path Found")
