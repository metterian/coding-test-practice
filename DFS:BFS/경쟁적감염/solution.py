#%%
n, k  = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
# %%
visited = [[0]*3 for _ in range(n)]
# %%
from collections import deque

def spread_virus(s):
    # global s
    queue  = deque()
    for i, cor in enumerate(virus_cor):
        queue.append([cor[0], cor[1], s, i+1])
        visited[cor[0]][cor[1]] = i+1



    while queue:
        mov_x, mov_y, mov_s, virus_key = queue.popleft()
        if  mov_s > 0 :
            #상
            if 0 <= mov_y - 1 < n and not visited[mov_x][mov_y-1] :
                visited[mov_x][mov_y-1] = virus_key
                queue.append([mov_x, mov_y-1, mov_s-1, virus_key])
            #하
            if  0 <= mov_y + 1 < n and not visited[mov_x][mov_y+1] :
                visited[mov_x][mov_y+1] = virus_key
                queue.append([mov_x, mov_y+1, mov_s-1, virus_key])
            #좌
            if 0<= mov_x - 1 < n and not visited[mov_x-1][mov_y] :
                visited[mov_x-1][mov_y] = virus_key
                queue.append([mov_x - 1, mov_y, mov_s-1, virus_key])

            if 0<= mov_x + 1 < n and not visited[mov_x+1][mov_y] :
                visited[mov_x+1][mov_y] = virus_key
                queue.append([mov_x+1, mov_y, mov_s-1, virus_key])

    return visited[x-1][y-1]




virus_cor = [0] *(k+1)
for row in range(n):
    for col in range(n):
        if graph[row][col] in virus:
            virus_cor[graph[row][col]] = [row, col]

virus_cor = sorted(virus_cor[1:])
print(spread_virus(s))

# %%
