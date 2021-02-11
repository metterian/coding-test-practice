#%%
row, col  = 5, 5
graph = [
[0, 0, 0, 0, 0],
[0, 0, 10, 10, 0],
[0, 10, 0, 10, 0],
[0, 0, 10, 10, 0],
[0, 0, 0, 0, 0],
]

visited = [[False] * (col) for _ in range(row)]
# %%
from collections import deque
# 동 서 남 북
dxs = [0, 0, 1, -1]
dys = [1, -1, 0,0 ]

def melting_glacier(graph):
    global dxs, dys, row, col
    melted = [[0] * (col) for _ in range(row)]

    for x in range(row):
        for y in range(col):
            sea_cnt = 0
            # 동 서 남 북 0 확인
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    if graph[nx][ny] == 0:
                        sea_cnt += 1

            melted[x][y] = graph[x][y] - sea_cnt
            if melted[x][y] < 0: melted[x][y] = 0

    return melted



""" Check for the glaciers are all melted. """
def check_melted(graph):
    for r in graph:
        if sum(r):
            return False

    return True


def bfs(graph, visited, start):
    global dxs, dys

    x, y = start
    visited[x][y] = True
    queue = deque([[x,y]])

    while queue:
        x,y = queue.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx,  y + dy
            if 0 <= nx < row and 0 <= ny < col:
                if not visited[nx][ny] and  graph[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

#%%
def solution(graph):
    global row, col

    year = 0
    divied = 0

    while True:
        divied = 0
        graph = melting_glacier(graph)
        if check_melted(graph):
            return 0

        visited = [[False] * (col) for _ in range(row)]

        for x in range(row):
            for y in range(col):
                if graph[x][y] != 0 and not visited[x][y]:
                    bfs(graph, visited, [x,y])
                    divied += 1
        if divied >= 2:
            return year

solution(graph)
# %%
