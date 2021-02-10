# %%
F,S,G,U,D = map(int, input().split())
limit = int(1e6)

# %%
from collections import deque

visited = [False] * (limit+1)
def bfs(F,S,G,U,D):
    counts = []
    btn_cnt = 0
    queue = deque([[S, btn_cnt]])

    while queue:
        now, btn_cnt = queue.popleft()
        up, down = now + U, now - D

        if now == G:
            counts.append(btn_cnt)
            continue

        if 1 <= up <= limit and up <= F:
            if not visited[up]:
                visited[up] = True
                queue.append([up, btn_cnt+1])

        if 1 <= down <= limit:
            if not visited[down]:
                visited[down] = True
                queue.append([down, btn_cnt+1])

    if counts:
        return counts
    else:
        return "use the stairs"

print(bfs(F,S,G,U,D))

# %%
