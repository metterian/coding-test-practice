#%%
# n, m = map(int, input().split())
n, m = 5, 17
# %%
from collections import deque

visited = [-1] * 100001



def bfs(start, visited, end):

    queue = deque([start])
    visited[start] = 0

    while queue:
        v = queue.popleft()
        if v == end:
            return visited[v]
        if 0<= v-1 <= 100000 and visited[v-1] == -1:
            visited[v-1] = visited[v] +1
            queue.append(v-1)

        if 0<= v+1 <= 100000 and  visited[v+1] == -1:
            visited[v+1] = visited[v] +1
            queue.append(v+1)



        if 0<= v*2 <= 100000 and visited[v*2] == -1:
            visited[v*2] = visited[v] +1
            queue.append(v*2)


bfs(n,visited, m)
# %%
n,m = map(int, input().split())
# %%
