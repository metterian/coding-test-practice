#%%
def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

# %%
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2, 6, 8],
    [1,7]
]
visited = [False] * len(graph)
#%%
dfs(graph, visited, 1)
# %%

# %%
