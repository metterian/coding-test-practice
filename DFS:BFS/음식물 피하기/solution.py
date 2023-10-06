#%%

import sys

sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
graph = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = True

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

def dfs(r, c):
    visited[r][c] = True
    cnt = 1

    for dr, dc in zip(dx, dy):
        nr, nc = r + dr, c + dc

        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc]:
            cnt += dfs(nr, nc)

    return cnt

max_size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            max_size = max(max_size, dfs(i, j))

print(max_size)








# %%
