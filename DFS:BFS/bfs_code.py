# %%
from collections import defaultdict, deque


def bfs(graph, visited, start):
    # graph에 연결된 노드를 방문한 다음
    queue = deque([start])
    visited[start] = True

    while queue:  # 큐가 빌 때까지 반복, 큐가 비면 False
        v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
        print(v, end=" ")
        for i in graph[v]:  # 그래프에 연결된 노드를 방문
            if not visited[i]:  # 방문하지 않은 노드라면
                visited[i] = True  # 방문 처리
                queue.append(i)  # 큐에 삽입


# %%
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]  # 각 노드가 연결된 정보를 표현 (2차원 리스트)
visited = [False] * len(graph)  # 방문 정보를 표현하는 리스트

bfs(graph, visited, 1)
# %%


# %%
