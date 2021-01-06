#%%
import math
INF = math.inf
route = [[5,1,15],[4,2,6],[1,4,8],[3,2,10],[1,2,7],[5,4,6],[2,5,11]]
# 노드, 간선 갯수
n ,m  = len(route)+1 , 3
# 2차원 dp 테이블을 만들고 모든 값을 INF 로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for row in range(1, n+1):
    for col in range(1, n+1):
        if col == row:
            graph[row][col] = 0

# 각 간선의 정보를 입력받아 그 값으로 초기화

# for _ in range(m):
#     a,b,c = map(int, input().split())
#     graph[a][b] = c


for s,d,w in route:
    graph[s][d] =w
# %%
""" 플로이드 알고리즘 수행 """
for k in range(1, n+1):
    for row in range(1, n+1):
        for col in range(1, n+1):
            graph[row][col] = min(graph[row][col], graph[row][k]+ graph[k][col])

# %%
""" 결과 출력 """
for row in range(1 , n+1):
    for col in range(1, n+1):
        if graph[row][col] == INF:
            print("INF", end= '\t')
        else:
            print(graph[row][col], end='\t')

    print()

# %%
