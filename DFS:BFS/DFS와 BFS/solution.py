
#%%
n, m , v = map(int, input().split())
graph = [[]  for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#%%
for i, value in enumerate(graph):
    graph[i] = sorted(value)

# %%
visited = [False] * (n+1)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for now in graph[v]:
        if not visited[now]:
            dfs(graph, now, visited)

dfs(graph, v, visited)
print()
# %%
from collections import deque
visited = [False] * (n+1)
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
bfs(graph, v, visited)
# %%
