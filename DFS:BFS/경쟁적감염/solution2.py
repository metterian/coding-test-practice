#%%
import sys
from typing import Coroutine
# input = sys.stdin.readline
n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, vx, vy = map(int, input().split())

visited = [[0] * n for _ in range(n) ]
start = []
for i in range(1, k+1):
    for row in range(n):
        for col in range(n):
            if i ==  graph[row][col]:
                start.append([row, col, graph[row][col], 0])

# %%
from collections import deque
def bfs(graph, start, visited):
    global s
    queue = deque(start)
    for r,c,v,t in start:
        visited[r][c] = v
    # 상 하 좌 우 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        row, col, virus, time = queue.popleft()
        if time >= s:
            break
        for x,y in zip(dx, dy):
            nx, ny = x + row, y + col
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = virus
                    queue.append([nx, ny, virus, time+1])



bfs(graph, start, visited)
print(visited[vx-1][vy-1])
# %%

# %%
