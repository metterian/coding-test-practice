
# %%
city_nodes, city_edges = map(int, input().rstrip().split())

city_from = [0] * city_edges
city_to = [0] * city_edges

for i in range(city_edges):
    city_from[i], city_to[i] = map(int, input().rstrip().split())

company = int(input().strip())
#%%

graph = [[] for _ in range(city_nodes+1)]
k = 0
for f,t in zip(city_from, city_to):
    graph[f].append(t)
    graph[t].append(f)

for i in range(city_nodes+1):
    graph[i].sort()
    

#%%
from collections import deque
visited = [False] * (city_nodes+1)
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
bfs(graph, 1, visited)
# %%
