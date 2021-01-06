#%%

n = 5
direction = list("R R R U D D".split())

    #[L, R, U, D]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x, y = 1,1

# %%
for direct in direction:
    for i in range(len(move_types)):
        if move_types[i] == direct:
            nx = x+ dx[i]
            ny = y+ dy[i]
    
    if nx <1 or nx > n or ny > n or ny <1 :
        continue
    x,y = nx, ny
print(x,y)

# %%
