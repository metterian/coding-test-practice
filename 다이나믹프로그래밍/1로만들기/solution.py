#%%
import math
n = 26
# %%
def solution(n: int) -> int:
    dp = [0] * (n+1)
    dp[1], dp[2], dp[3], dp[5] = 1,1,1,1
    dp[4] = 2
    for i in range(6, n+1):
        two, three, five, one = [math.inf] *4
        if i % 2 == 0 :
            two = dp[i//2] + 1
        if i%3 == 0:
            three = dp[i//3] +1
        if i%5 == 0:
            five = dp[i//5] +1
        one = dp[i-1] + 1
        dp[i] = min(two, three, five, one)

    return (dp[n])
solution(n)
# %%
