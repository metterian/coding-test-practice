#%%
m, n, k = map(int, input().split())
rect = []
for _ in range(k):
    a,b,c,d = map(int, input().split())
    # 좌표 변환
    # 하안: (row - y - 1, x)
    # 상안: (col - y, x-1)
    rect.append([m-b-1, a, abs(m-d), c-1])

# %%
visited = [[False] * n for _ in range(m)]
for a,b,c,d in rect:
    max_row ,min_row = max(a,c), min(a,c)
    max_col, min_col = max(b,d), min(b,d)

    for r in range(min_row, max_row+1):
        for c in range(min_col, max_col + 1):
            visited[r][c] = True



# %%
from collections import deque

def bfs(visited, start):
    r, c = start
    visited[r][c] = True
    queue = deque([[r,c]])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    area = 1

    while queue:
        r,c = queue.popleft()
        for x, y in zip(dx,dy):
            nx = r + x
            ny = c + y
            if 0<= nx < m and 0<= ny < n:
                if not visited[nx][ny]:
                    area += 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    return area

division = 0
areas = []
for r in range(m):
    for c in range(n):
        if not visited[r][c]:
            areas.append(bfs(visited, [r,c]))
            division += 1

print(division)
areas.sort()
for area in areas:
    print(area, end=' ')

# %%
