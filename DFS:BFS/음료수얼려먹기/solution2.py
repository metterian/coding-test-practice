#%%
from pprint import pprint

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))



def dfs(row, col):
    if row < 0 or row >= n or col < 0 or col >= m:
        return False

    if graph[row][col] == 0:
        graph[row][col] = 1
        dfs(row=row+1, col=col) # 상
        dfs(row=row-1, col=col) # 하
        dfs(row=row, col=col-1) # 좌
        dfs(row=row, col=col+1) # 우
        return True
    return False

result = 0
for r in range(n):
    for c in range(m):
        if dfs(row=r, col=c) == True:
            result += 1



print(result)
