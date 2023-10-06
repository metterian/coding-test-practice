from collections import deque
from pprint import pprint

n, m = map(int, input().split())
queue = deque()

graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))


def bfs(row, col):
    queue = deque()
    queue.append([row, col])

    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문 하는 경우 -> 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
    return graph


graph = bfs(0,0)
print(graph[n-1][m-1])

