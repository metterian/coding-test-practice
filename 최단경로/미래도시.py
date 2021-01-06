#%%
import math
INF = math.inf

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b], graph[b][a] = 1,1

x, k = map(int, input().split())


for row in range(1, n+1):
    for col in range(1, n+1):
        if row == col: graph[row][col] = 0

# %%
for k in range(1, n+1):
    for row in range(1, n+1):
        for col in range(1, n+1):
            graph[row][col] = min(graph[row][col], graph[row][k]+graph[k][col])

# %%
result  = graph[1][k] + graph[k][x]
if result >= INF:
    print("-1")
else:
    print(result)
# %%
