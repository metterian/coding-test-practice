#%%

#%%
num = 0


from collections import deque
direct = deque([[1,0],[0,1],[-1,-1]])


def visited_all(graph):
    for row in graph:
        for value in row:
            if not value:
                return False

    return True

def dfs(visited, graph, start, n, direct):
    global num

    if visited_all(graph): return graph
    num += 1
    row, col = start
    visited[row][col] = True
    graph[row][col] = num




    dx,dy = direct[0]
    nx, ny = dx + row, dy + col
    while not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
        direct.append(direct.popleft())
        dx,dy = direct[0]
        nx, ny = dx + row, dy + col

    if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny]:
            dfs(visited, graph, [nx,ny], n, direct)





    return graph


def solution(n):
    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for row in range(n-1):
        for col in range(row+1, n):
            visited[row][col] = True
    answer = dfs(visited, graph, [0,0], n, direct)
    return answer

solution(5)

# %%

# %%
