#%%
n = 5
tree = []
tree.append(0)
for _ in range(n):
    tree.append(list(map(int, input().split())))


#%%
def solution (tree):
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[1][1] = tree[1][0]
    for r in range(2, n+1):
        for c in range(1, len(tree[r])+1):
            dp[r][c] = max(dp[r-1][c-1], dp[r-1][c]) + tree[r][c-1]
    return max(dp[-1])
solution(tree)




# %%
