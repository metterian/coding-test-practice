#%%
"""

maps	answer
[[1,0,1,1,1],
[1,0,1,0,1],
[1,0,1,1,1],
[1,1,1,0,1],
[0,0,0,0,1]]	11
[[1,0,1,1,1],
[1,0,1,0,1],
[1,0,1,1,1],
[1,1,1,0,0],
[0,0,0,0,1]]	-1
"""
#%%

from collections import deque


# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    i, j = start
    queue = deque([[i,j, 1]])
    # 현재 노드를 방문 처리
    visited[i][j] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        i, j, step = queue.popleft()
        if [i,j] == end_point:
            return step
        if end_point[0] >= i+1 >= 0  and end_point[1]>=j >=0 :
            if not visited[i+1][j] and graph[i+1][j]:
                queue.append([i+1, j, step+1])
                visited[i+1][j] = True
        if end_point[0] >= i >= 0  and end_point[1]>= j+1 >= 0 :
            if not visited[i][j+1] and graph[i][j+1]:
                queue.append([i, j+1, step+1])
                visited[i][j+1] = True
        if end_point[0] >= i-1 >= 0  and end_point[1]>= j >=0 :
            if not visited[i-1][j] and graph[i-1][j]:
                queue.append([i-1, j, step+1])
                visited[i-1][j] = True
        if end_point[0] >= i >= 0  and end_point[1]>= j-1 >=0 :
            if not visited[i][j-1] and graph[i][j-1]:
                queue.append([i, j-1, step+1])
                visited[i][j-1] = True
    return -1
# %%
maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]
# %%
from copy import deepcopy

visited = deepcopy(maps)
for i, row in enumerate(visited):
    for j, col in enumerate(row):
        visited[i][j] = False

end_point = [len(maps)-1, len(maps[0])-1]
solution = 0
# %%
bfs(graph=maps, start=[0,0], visited=visited)
#%%

