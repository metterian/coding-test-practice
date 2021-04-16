#%%
n,m = 4, 5
graph = [
'c.xc',
'....',
'xx..',
'...x',
'x..x',
]

# %%
from collections import deque

# 아래, 좌, 우,
dx = [1,0,0]
dy = [0,-1,1]

# 최단경로수, 움직임
data = []
mov = 0
left, right = 0,0
flag = True
def dfs(graph, visited, start):
    global mov, left, right,flag

    r, c = start
    if r == m-1 and flag:
        flag = False
        data.append([mov, abs(left-right)])
        mov, left, right = 0,0,0
        return
    elif r == m-1 and not flag:
        return
    visited[r][c] = True

    for x,y in zip(dx,dy):
        nx = x + r
        ny = y + c
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == '.':

                if [x,y] == [0,-1]:
                    left += 1
                if [x,y] == [0,1]:
                    right += 1
                visited[nx][ny] = True
                mov += 1
                dfs(graph, visited, [nx,ny])

#%%
def solution(m,n):
    global mov, right, left, flag
    for row in range(m):
        for col in range(n):
            if graph[row][col] == 'c':
                mov = 0
                left = 0
                right = 0
                visited = [[False] * n for _ in range(m)]
                flag =True
                dfs(graph, visited, [row,col])

    return min(data)[1]

solution(m,n)



# %%

# %%
