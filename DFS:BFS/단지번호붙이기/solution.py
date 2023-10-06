from pprint import pprint

n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


def dfs(r, c):
    visited[r][c] = True

    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cnt = 1

    for dr, dc in direction:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if not visited[nr][nc] and graph[nr][nc]:
            cnt += dfs(nr, nc)

    return cnt


count = []
for r in range(n):
    for c in range(n):
        if not visited[r][c] and graph[r][c]:
            cnt = dfs(r, c)
            count.append(cnt)

print(len(count))
for cnt in sorted(count):
    print(cnt)
