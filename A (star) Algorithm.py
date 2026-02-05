def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {start: 0}
    while open_list:
        _, current = heapq.heappop(open_list)   
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 0):
                tentative_g = g_cost[current] + 1
                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g
                    f_cost = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None


warehouse = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)   
goal = (4, 4)   
path = a_star(warehouse, start, goal)

if path:
    print("Shortest path found:")
    for step in path:
        print(step)
else:
    print("No path found")

import matplotlib.pyplot as plt
plt.plot([p[1] for p in path], [p[0] for p in path], marker='o')
