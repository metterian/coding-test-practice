#%%
a = [-5,0,2,1,2]
edges =[[0,1],[3,4],[2,3],[0,3]]


#%%
from collections import Counter
from itertools import chain

def solution(a, edges):
    answer = 0
    edges_count = Counter(chain(*edges)).most_common()

    graph = [[] for _ in range(len(a))]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)


    for edge, _ in edges_count:
        if not a[edge]:
            continue

        for now in graph[edge]:
            if a[now] == 0:
                continue
            elif a[now] > 0:
                a[edge] += a[now]
                answer += abs(a[now])
                a[now] = 0
            else:
                a[edge] += a[now]
                answer += abs(a[now])
                a[now] = 0

    # print(a)

    return answer

solution(a, edges)
# %%
