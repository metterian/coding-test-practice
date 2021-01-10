#%%
n, m = 6,4
graph = [
[0, -1, 0, 0, 0, 0],
[-1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
]
visited = [[False] * n for _ in range(m)]
start = []
for row in range(m):
    for col in range(n):
        if graph[row][col] == 1:
            start.append([col, row])
# %%
from collections import deque


def bfs(graph, start, visited):
    date = 0
    queue = deque()
    for x,y in start:
        visited[y][x] = True
        queue.append([x,y, date])

    # 왼쪽, 오른쪽, 앞, 뒤 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, +1]

    while queue:
        x, y, date = queue.popleft()
        for a, b in zip(dx, dy):
            nx, ny = x + a, y + b
            if 0 <= nx < n and 0 <= ny < m and 0 <= graph[ny][nx]:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    graph[ny][nx] = 1
                    queue.append([nx, ny, date+1])

    for row in graph:
        if 0 in row:
            return -1
    return date


result = bfs(graph, start, visited)
print(result)
# %%

# %%
