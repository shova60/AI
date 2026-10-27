
from collections import deque
import heapq

# Input Tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# 1. Breadth-First Search (BFS)
def bfs(tree, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)

        for child in tree[node]:
            queue.append(child)

    return visited


# 2. Depth-First Search (DFS)
def dfs(tree, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(tree[node]))

    return visited


# 3. Depth-Limited Search (DLS)
def dls(tree, node, limit):
    if limit < 0:
        return []

    result = [node]

    if limit == 0:
        return result

    for child in tree[node]:
        result.extend(dls(tree, child, limit - 1))

    return result


# 4. Iterative Deepening DFS (IDDFS)
def iddfs(tree, start, max_depth):
    results = []

    for depth in range(max_depth + 1):
        results.append((depth, dls(tree, start, depth)))

    return results


# 5. Uniform Cost Search (UCS)
weighted_graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2), ('G', 5)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for child, edge_cost in graph[node]:
            if child not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, child, path + [child])
                )

    return None, float('inf')


# Display Results
print("INPUT TREE:")
print(tree)

print("\n1. BFS Traversal:")
print(bfs(tree, 'A'))

print("\n2. DFS Traversal:")
print(dfs(tree, 'A'))

print("\n3. DLS Traversal (Depth Limit = 2):")
print(dls(tree, 'A', 2))

print("\n4. IDDFS Traversal:")
for depth, result in iddfs(tree, 'A', 2):
    print(f"Depth {depth}: {result}")

print("\n5. UCS (Start = A, Goal = G):")
path, cost = ucs(weighted_graph, 'A', 'G')
print("Path:", path)
print("Total Cost:", cost)
