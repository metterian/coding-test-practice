#%%
t =  3
# %%

def fibonacci(n):

    dp = [[0,0]] * (n+2)
    dp[0] = 1,0
    dp[1] = 0,1
    if n < 2:
        return dp[n]
    for i in range(2, n+1):
        a,b = dp[i-1]
        c,d = dp[i-2]
        dp[i] = a+c, b+d
    return dp[n]



for _ in range(t):
    n = int(input())
    for i in fibonacci(n):
        print(i, end=' ')
    print()




# %%

# %%
