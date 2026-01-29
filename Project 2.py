# For BFS
city_map = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

from collections import deque

def bfs_city_traversal(city_map, start):
    visited = set()
    queue = deque([start])
    print("BFS Traversal Order:")
    while queue:
        intersection = queue.popleft()
        if intersection not in visited:
            print(intersection, end=" ")
            visited.add(intersection)
            for neighbor in city_map[intersection]:
                if neighbor not in visited:
                    queue.append(neighbor)

bfs_city_traversal(city_map, 'A')

bfs_city_traversal(city_map, 'B')

bfs_city_traversal(city_map, 'C')

bfs_city_traversal(city_map, 'E')

# For DFS
city_map = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

def dfs_city_traversal(city_map, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=" ")
    visited.add(start)
    for neighbor in city_map[start]:
        if neighbor not in visited:
            dfs_city_traversal(city_map, neighbor, visited)

print("DFS Traversal Order:")
dfs_city_traversal(city_map, 'A')
