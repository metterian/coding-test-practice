#%%
n = 7
array = [15, 11, 4, 8, 5, 2, 4]
dp = [1] * n

# %%
def solution(n):
    array.reverse()
    for i in range(n):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return n - max(dp)


print(solution(n))
# %%
