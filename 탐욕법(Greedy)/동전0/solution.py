#%%
n, k = map(int, input().split())
coins = []
for _ in range(n):
    num = int(input())
    if num <= k: coins.append(num)

#%%
count = 0
for coin in coins[::-1]:
    quo = k // coin
    count += quo
    k -= quo * coin

print(count)
# %%
