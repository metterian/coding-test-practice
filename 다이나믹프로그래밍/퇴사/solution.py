#%%
n = 10
table = [
[0,0],
[5, 50],
[4, 40],
[3, 30],
[2, 20],
[1, 10],
[1, 10],
[2, 20],
[3, 30],
[4, 40],
[5, 50]
]

# %%
dp = [[] for _ in range(n+1)]
for i, value in enumerate(table):
    day, price = value
    for j in range(i+day+1, n+1):
        dp[j].append(day)


# %%
