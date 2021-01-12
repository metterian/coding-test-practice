#%%
n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
# %%
def solution(n):
    if n == 1:
        return stairs[1]
    dp = [[0,0] for _ in range(n+2)]
    # [한칸씩 올라오는 경우, 두칸씩 올라오는 경우]
    dp[1] = stairs[1], 0
    dp[2] = stairs[1] + stairs[2], stairs[2] # [한칸씩 올라오는 경우, 두칸씩 올라오는 경우]

    for i in range(3, n+1):
        # 한칸 아래에서 올라 오는 경우 -> 한 칸전에 두칸에서 올라온 경우만 고려(연속 3칸 X)
        one_step = dp[i-1][1] + stairs[i]
        # 두칸 아래에서 올라오는 경우 -> 두 칸 전에 가장큰 수
        two_step = max(dp[i-2]) + stairs[i]
        dp[i] = one_step, two_step

    return max(dp[n])

print(solution(n))
# %%

