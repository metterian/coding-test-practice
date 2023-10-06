#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    DFS(깊이 우선 탐색)은 그래프나 트리를 탐색하는 알고리즘 중 하나로,
#    루트 노드(혹은 다른 임의의 노드)에서 시작하여 마지막 노드까지 깊이를 우선하여 탐색하는 알고리즘입니다.
#    스택을 사용하여 구현할 수 있으며, 아래 코드는 스택을 사용한 방법으로 DFS를 구현한 예입니다.

# 2. 예시 입력 / 출력:
#    입력: graph = {1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, start_node = 1
#    출력: 1 3 2 5 4

# 3. 알고리즘의 시간 복잡도:
#    O(V + E) (V: 정점의 개수, E: 간선의 개수)

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 경로 찾기
#    - 사이클 탐지
#    - 그래프 연결 성분 찾기

#%%

def dfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    stack = [start_node]

    while stack:
        node = stack.pop()

        if not visited[node] :
            visited[node] = True;
            print(node, end=' ')
            # for adj_node in graph[node]: # 인접한 노드 방문
            for adj_node in reversed(graph[node]): # 인접한 노드 방문
                if not visited[adj_node]:
                    stack.append(adj_node)


# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# DFS 알고리즘 실행
dfs(graph, 1) # 1 3 2 5 4
#%%


# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# DFS 알고리즘 실행
dfs(graph, 1) # 1 3 2 5 4

# %%
