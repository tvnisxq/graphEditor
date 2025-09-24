from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(n for n in graph.neighbours(node) if n not in visited)

            yield visited[:] # yield a snapshot after each visit


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    yield visited[:]

    for neighbour in graph.neighbours(start):
        if neighbour not in visited:
            yield from dfs(graph, neighbour, visited)
