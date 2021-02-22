#%%
n,m  = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)]



from itertools import permutations, combinations, product
from collections import deque
import copy

pro_coord = list(product(range(max(n,m)), repeat=2))
coord = []
for r, c in pro_coord:
    if r < n and c < m:
        coord.append([r,c])
barriers = list(combinations(coord, 3))


def get_safe_area(graph):
    score = 0
    for i in range(n):
        for j in range(m):
            if not graph[i][j]:
                score += 1
    return score

#%%
def virus(graph, visited, start):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r,c = start
    queue = deque([[r,c]])

    while queue:
        r, c = queue.popleft()
        for x, y in zip(dx,dy):
            nx = r + x
            ny = c + y
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = 2
                    queue.append([nx, ny])

area = []
visit = [[False]*m for _ in range(n)]
for barrier in barriers:
    graph = copy.deepcopy(lab)
    visited = copy.deepcopy(visit)
    for bx, by in barrier:
        graph[bx][by] = 1
    for r in range(n):
        for c in range(m):
            if lab[r][c] == 2 and not visited[r][c]:
                virus(graph, visited, [r,c])
    area.append(get_safe_area(graph))
print(max(area))
# %%


# %%
