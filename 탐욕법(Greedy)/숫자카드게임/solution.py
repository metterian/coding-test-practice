#%%
n, m  = list(map(int, '2 4'.split()))
matrix =  [list(map(int, input().split())) for _ in range(n)]
# %%
mins = [min(row) for row in matrix]
print(max(mins))

# %%
