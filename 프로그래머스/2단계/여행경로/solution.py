#%%
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

#%%
def visitCheck(visited):
    return len(visited) == sum(visited.values())


def dfs(graph, v, visited):

    start, end = v
    visited["-".join([start, end])] = True
    result.append(start)
    if visitCheck(visited):
        return

    for now in graph[v]:
        if not visited[now]:
            dfs(graph, [now, graph[now]], visited)


#%%
def solution(tickets):
    global result, routes
    routes = {}
    for ticket in tickets:
        start, end = ticket
        routes[start] = routes.get(start, []) + [end]
        routes[start] = sorted(routes[start], reverse=True)

    visit = {}
    for ticket in tickets:
        visit["-".join(ticket)] = False

    for end in routes["ICN"]:
        result = ["ICN"]
        visited = visit
        visited["-".join(["ICN", end])] = True
        dfs(routes, [end, routes[end]], visited)

    return result


solution(tickets)

# %%
from collections import defaultdict


def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for country in graph:
        a, b = country
        if not visited[a]:
            print(a)
            dfs(graph, visited, b)

flights = defaultdict(list)
for src, dst in sorted(tickets, reverse=True):
    flights[src].append(dst)


for i, ticket in enumerate(tickets):
    tickets[i] = sorted(ticket, reverse=True)



dfs(tickets, visited, "ICN")

# %%
