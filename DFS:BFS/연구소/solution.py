#%%
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


# %%
# Virus Spread Direction
dx = [-1, 1, 0,0]
dy = [0, 0, -1, 1]


visited =[[False]*m for _ in range(n)]

from collections import deque

def getSafeZone(graph, infected):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if not infected[r][c] and graph[r][c]==0:
                cnt+=1

    return cnt

def spreadVirus(graph,infected, start):
    global n,m

    r,c = start
    queue = deque([start])
    infected[r][c] = True

    while queue:
        r,c = queue.popleft()
        for x, y in zip(dx,dy):
            nx, ny = r+x, c+y
            if 0 <= nx < n and 0 <= ny < m:
                if not infected[nx][ny] and graph[nx][ny] == 0:
                    infected[nx][ny] = True
                    queue.append([nx,ny])

def virus(infected):
    global n,m
    for r in range(n):
        for c in range(m):
            if not infected[r][c] and graph[r][c] == 2:
                spreadVirus(graph,infected, [r,c])

depth = 0
zone = 0
def dfs(graph):
    global depth, zone
    if depth >= 3:
        infected = [[False]*m for _ in range(n)]
        virus(infected)
        zone = max(zone, getSafeZone(graph,infected))
        return
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and graph[r][c] == 0:
                visited[r][c] = True
                graph[r][c] = 1
                depth += 1
                # 실행
                dfs(graph, [r, c])

                graph[r][c] = 0
                depth -= 1
                visited[r][c] = False




dfs(graph)
print(zone)

# %%
