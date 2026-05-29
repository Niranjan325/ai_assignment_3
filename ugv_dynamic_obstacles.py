import random
import heapq

GRID_SIZE = 20

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
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

            if (0 <= neighbor[0] < GRID_SIZE and
                0 <= neighbor[1] < GRID_SIZE and
                grid[neighbor[0]][neighbor[1]] == 0):

                temp = g_score[current] + 1

                if neighbor not in g_score or temp < g_score[neighbor]:
                    g_score[neighbor] = temp
                    f = temp + heuristic(neighbor, goal)

                    heapq.heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current

    return None

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for _ in range(60):
    x = random.randint(0, GRID_SIZE-1)
    y = random.randint(0, GRID_SIZE-1)
    grid[x][y] = 1

start = (0,0)
goal = (19,19)

path = astar(grid, start, goal)

if path:
    print("Initial Path Found")

    if len(path) > 5:
        obstacle = path[5]
        grid[obstacle[0]][obstacle[1]] = 1

        print("Dynamic obstacle introduced at:", obstacle)
        print("Replanning...")

        new_path = astar(grid, start, goal)

        if new_path:
            print("New Path Found")
            print(new_path)
        else:
            print("No Alternate Path")
else:
    print("No Path Exists")
