#%%
rows = 4

cols = 4

initR = 1

initC = 2

finalR = 3

finalC = 3


costRows = [1,2,3]
costCols = [7,8,9]

# %%
delta_row = abs(initR - finalR)
delta_col = abs(initC - finalC)
count = delta_col + delta_row

r, c = initR, initC
cost = 0
while count:
    if r < finalR and costRows[r] < costCols[c] :
        cost += costRows[r]
        r += 1
    else:
        cost += costCols[c]
        c += 1

    count -= 1

print(cost)
# %%
