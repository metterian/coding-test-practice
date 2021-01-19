# %% [markdown]
### 상향식
# %%
from collections import defaultdict

n = 10
dp = defaultdict(int)
def fib(n):

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

fib(n)
# %% [markdown]
### 하향식
# - 하위 문제에 대한 정답을 계산 했는지 확인 해가며 **재귀** 형태로 문제를 해결해 나감
# %%
dp = defaultdict(int)
def fib(n):
    if n <= 1:
        return n

    if dp[n]:
        return dp[n]

    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
fib(10)
# %%
