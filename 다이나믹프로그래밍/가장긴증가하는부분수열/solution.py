#%%
from collections import defaultdict
n = 6
array = list(map(int, '10 20 10 30 20 50'.split()))
dp = [1] * n
# %%
def solution(n):
    for i in range(n):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


solution(n)
# %%
