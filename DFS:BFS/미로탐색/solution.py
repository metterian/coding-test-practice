#%%
n ,m = 4,6
graph = [
[1,1,0,1,1,0],
[1,1,0,1,1,0],
[1,1,1,1,1,1],
[1,1,1,1,0,1],
]
visited = [[False] * m for _ in range(n)]
# %%
def dfs(graph, now, visited):
    row, col, block = now
    visited[row][col] = True

    if row == n-1 and col == m-1:
        print(block)


    # 서로 인전한 칸 이동 정의
    # 동 남 북 서
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    for x, y in zip(dx,dy):
        nx = row + x
        ny = col + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(graph, [nx,ny, block+1], visited)
dfs(graph, [0,0,1], visited)
# %%

# 최단 시간 소요는 깊이 우선 탐색 보다는 너비 우선 탐색이 적절함
from collections import deque
def bfs(graph, start, visited):
    row, col, block = start
    visited[row][col] = True

    queue = deque([start])

    # 서로 인전한 칸 이동 정의
    # 동 남 북 서
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while queue:
        row, col, block = queue.popleft()
        if row == n-1 and col == m-1:
            print(block)
            break
        for x, y in zip(dx,dy):
            nx = row + x
            ny = col + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx,ny, block+1])
bfs(graph, [0,0,1], visited)
# %%
# %%
