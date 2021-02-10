#%%
import math
n = 5
graph = [
    [6, 8, 2, 6, 2],
    [3, 2, 3, 4, 6],
    [6, 7, 3, 3, 2],
    [7, 2, 5, 3, 6],
    [8, 9, 5, 2, 7],
]

visited = [[False] * (n) for _ in range(n)]

max_height = max([max(row) for row in graph])
safe_zone = -math.inf
# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#%%
from collections import deque
def set_rain(visited, rain_height):

    for row in range(n):
        for col in range(n):
            if graph[row][col] <= rain_height:
                visited[row][col] = True
    return visited


def bfs(graph, visited, start):
    global dx, dy

    x,y = start
    queue = deque([[x,y]])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for a,b in zip(dx, dy):
            nx = x + a
            ny = y + b
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])



def solution(graph, visited, max_height, n):
    global safe_zone
    for h in range(1, max_height+1):
        visited = [[False] * (n) for _ in range(n)]
        zone = 0
        sinked = set_rain(visited, h)
        for row in range(n):
            for col in range(n):
                if not sinked[row][col]:
                    zone += 1
                    bfs(graph, visited = sinked, start=[row,col])

        safe_zone = max(safe_zone, zone)

    return safe_zone

solution(graph, visited, max_height, n)
if not safe_zone:
    print(1)
else:
    print(safe_zone)

