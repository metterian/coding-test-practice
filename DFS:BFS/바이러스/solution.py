from collections import defaultdict
from pprint import pprint

num_of_pc = int(input())
n = int(input())


location = []
for _ in range(n):
    location.append(list(map(int, input().split())))


graph = defaultdict(list)

for r, c in location:
    graph[r].append(c)
    graph[c].append(r)


visited = [False] * (num_of_pc + 1)


def dfs(node, visited):
    visited[node] = True
    cnt = 1
    # print(f"node: {node}", end="\n")

    for adj in graph[node]:
        if not visited[adj]:
            cnt += dfs(adj, visited)

    # print(f"cnt: {cnt}")
    return cnt


cnt = dfs(1, visited)
print(cnt - 1)
