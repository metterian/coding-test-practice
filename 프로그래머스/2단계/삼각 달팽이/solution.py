#%%

#%%
num = 0
from collections import deque
direct = deque([[1,0],[0,1],[-1,-1]])

def dfs(visited, graph, start, n, direct):
    global num

    num += 1
    x, y = start
    visited[x][y] = True
    graph[x][y] = num

    dx, dy = direct[0]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
        direct.rotate(-1)
        dx, dy = direct[0]
        nx, ny = x + dx, y + dy


    if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny]:
            dfs(visited, graph, [nx,ny], n, direct)





def solution(n):
    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for row in range(n-1):
        for col in range(row+1, n):
            visited[row][col] = True
    dfs(visited, graph, [0,0], n, direct)

    answer = []
    for row in range(n):
        for col in range(n):
            if graph[row][col]:
                answer.append(graph[row][col])

    return answer

solution(5)

# %%

# %%
