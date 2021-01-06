#%%
n , m = 4,5
M = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

# %%
def dfs(x,y):
    if x>=n or y>=5 or x<0 or y<0:
        return False

    if M[x][y] == 0:
        M[x][y] = 1
        #상
        dfs(x-1,y)
        #하
        dfs(x+1, y)
        #좌
        dfs(x, y-1)
        #우
        dfs(x, y+1)
        return True
    return False
# %%
answer = 0

for r in range(n):
    for c in range(m):
        if dfs(r,c):
            answer +=1

print(answer)

# %%
