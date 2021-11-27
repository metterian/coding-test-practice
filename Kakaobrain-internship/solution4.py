"""
일부 차단된 세포(#')와 차단되지 않은 세포('.')로 구성된 2-D 격자가 제공된다.
포인터의 시작 위치는 그리드의 왼쪽 상단 모서리에 있습니다. 시작 위치가 차단되지 않은 셀에 있음을 보증합니다.
오른쪽 아래 셀의 차단이 해제되는 것도 보장된다. 그리드의 각 셀은 오른쪽, 왼쪽, 위쪽 및 아래쪽 셀과 연결됩니다.
포인터가 셀에서 셀로 이동하는 데는 1초가 걸립니다.
포인터가 "k"초 이내에 그리드의 오른쪽 하단 모서리에 도달할 수 있으면 문자열 'Yes'를 반환합니다.
"""


#%%
input = open('input.txt', 'r').readline

grid_count = int(input().strip())

grid = []

for _ in range(grid_count):
    grid_item = input().strip()
    grid.append(grid_item)

maxTime = int(input().strip())

# %%



# %%
start = [0, 0]
time = 0
dx = [-1, 1, 0,0]
dy = [0, 0, -1, 1]

flag = False
times = []
from collections import deque
def bfs(graph, start, visited):
    global time, maxTime

    queue = deque([start])
    r, c, t = start
    visited[r][c] = True
    while queue:
        r, c, t = queue.popleft()
        for x, y in zip(dx,dy):
            nx, ny = r+x, c+y
            if 0 <= nx < grid_count and 0 <= ny < len(grid_item):
                if nx == grid_count-1 and ny == len(grid_item)-1:
                    times.append(t+1)
                # print(nx, ny)
                if not visited[nx][ny] and graph[nx][ny] == '.' and time <= maxTime:
                    visited[nx][ny] = True
                    time += 1
                    queue.append([nx,ny, t+1])


def reachTheEnd(grid, maxTime):
    visited = [[False] * len(grid_item)  for _ in range(grid_count)]
    bfs(grid, [0,0,0], visited)
    print(times)
    # if time <= maxTime and visited[grid_count-1][len(grid_item)-1]:
    #     return "Yes"
    # else:
    #     return "No"
    if min(times) <= maxTime:
        return "Yes"
    else:
        return "No"
reachTheEnd(grid, maxTime)
#%%


119546
