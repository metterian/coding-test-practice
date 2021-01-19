#%%
n = 10
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
[1, 10],
]
# %%
dp = [[0] for _ in range(n+1)]
dp2 = [0] * (n+1)
for day, value in enumerate(table):
    period, price = value
    # 1일 부터 시작
    if day == 0:
        continue
    # 현재 날짜 + 상담기간 보다 큰 경우 무시
    if day + period - 1 > n:
        continue

    max_price = max(dp[day])+price
    dp[day].append(max_price)
    for j in range(day +period, n+1):
        dp[j].append(price)
        dp[j].append(max_price)

    dp2[day] = max(dp[day])


max(dp2)

