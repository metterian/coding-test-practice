#%%
from collections import deque

n, k = map(int, input().split())

visited = [[0] * n for _ in range(n) ] # 바이러스에 대한 정보를 담는 리스트
graph = [] # 전체 보드 정보를 담는 리스트
start = [] # 시작 위치 정보를 담는 리스트

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 시작 위치 저장
for row in range(n):
    for col in range(n):
        if graph[row][col]:
            start.append([row, col, graph[row][col], 0])

s, vx, vy = map(int, input().split())
# %%
def bfs(graph, start, visited):
    global s
    # 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
    start = sorted(start, key=lambda x: x[2])
    queue = deque(start)

    # 행,열, 바이러스 정보, 담긴 시간 순으로 정보 저장
    for r,c,v,t in start:
        visited[r][c] = v
    # 상 하 좌 우 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        # 행,열, 바이러스 정보, 담긴 시간
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

