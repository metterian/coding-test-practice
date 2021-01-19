#%%
n = 10
table = []

for _ in range(n):
    x,y = map(int, input().split())
    table.append([x,y])

# %%
def solution(n):
    dp = [0] * (n+1)
    max_value = 0
    for i in range(n-1, -1, -1):
        t, p = table[i] #소요 시간, 비용

        time = t + i
        if time <= n :
            dp[i] = max(p + dp[time], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value

    return max(dp)
solution(10)
# %%

