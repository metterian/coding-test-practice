#%%
from collections import deque


n, m, k, start = list(map(int, input().split()))
# graph =[
#     [],
#     [2,3],
#     [3,4],
#     [],
#     []
# ]

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)


visited = [False] * (n+1)
distance = [0] * (n+1)
dist = 0
# %%

queue = deque([start])
visited[start] = True
while queue:
    v = queue.popleft()

    for i in graph[v]:
        if not visited[i]:
            visited[i]= True
            distance[i] = distance[i] + distance[v]
            queue.append(i)
#%%
flag = 1
for i in range(1,n+1):
    if distance[i] == k:
        flag = 0
        print(i)
if flag:
    print(-1)
        
# %%
