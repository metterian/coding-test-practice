# n = int(input())
# table = [[0,0]]
# for _ in range(n):
#     table.append(list(map(int, input().split())))


table = [
[0,0],
[1, 1],
[1, 2],
[1, 3],
[1, 4],
[1, 5],
[1, 6],
[1, 7],
[1, 8],
[1, 9],
[1, 10]
]

dp = [[0] for _ in range(n+1)]
for i, value in enumerate(table):
    if i == 0:
        continue
    day, price = value
    max_price = max(dp[i])+price
    dp[i].append(max_price)
    for j in range(i+day, n+1):
        dp[j].append(price)
        dp[j].append(max_price)


# %%
for i in range(n-1,0,-1):
    if i + table[i][0] <= n+1:
        print(max(dp[i]))
        break
