
input = open('input.txt', 'r').readline

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


for i, value in enumerate(graph):
    graph[i] = sorted(value)

visited = [False for _ in range(N+1)]

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for now in graph[v]:
        if not visited[now]:
            dfs(graph, now, visited)

dfs(graph, V, visited)
print()

visited = [False for _ in range(N+1)]
def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        now = queue.popleft()
        visited[now] = True
        print(now, end=' ')
        for v in graph[now]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

bfs(graph, V, visited)


