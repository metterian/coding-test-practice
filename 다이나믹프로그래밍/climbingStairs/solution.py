#%%

def climbingStairs(n):
    dp = [0] * (n+1)
    if n == 1:
        return 1
    if n== 2:
        return 2
    dp[2] = 2
    dp[1] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1]  + dp[i-2]
    return dp[n]

climbingStairs(1)
# %%
dp = [0] * (6+1)
# %%
