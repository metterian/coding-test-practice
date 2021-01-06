#%%

n = 5
direction = list("R R R U D D".split())
matrix = []

for row in range(1,n+1):
    rows = []
    for col in range(1,n+1):
        rows.append([row, col])
    matrix.append(rows)

start = [1,1]
for direct in direction:
    if direct == 'R':
        if 1<= start[1]+1 <=n:
            start[1]+=1
    elif direct == 'D':
        if 1<= start[0]+1 <=n:
            start[0]+=1

    elif direct == 'U':
        if 1<= start[0]-1 <=n:
            start[0]-=1

    elif direct == 'L':
        if 1<= start[1]-1 <=n:
            start[1]-=1



print(start)



for row in matrix:
    print(row)
# %%
