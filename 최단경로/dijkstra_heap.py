#%%
import sys, math, heapq
# input = sys.stdin.readline
INF = math.inf

# 노드의 갯수, 간선의 갯수
route = [[5,1,15],[4,2,6],[1,4,8],[3,2,10],[1,2,7],[5,4,6],[2,5,11]]
# 노드, 간선 갯수
n ,m  = len(route) , 3

#시작 노드
# start = int(input())
start = 1
graph = [[INF] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for s,d,w in route:
    graph[s][d] =w

#%%
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q) # dist: 햔재 노드에서 weight, now: 현재노드
        if now is INF or dist > distance[now]:
            continue
        for n, w in graph[now]:
            cost = w + dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

dijkstra(start)
# %%
print("INFINITY") if INF in distance[1:] else print(distance[1:])
# %%
