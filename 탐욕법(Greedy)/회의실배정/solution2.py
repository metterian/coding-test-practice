#%%
n = 11
schedules = [
    [1, 4],
    [3, 5],
    [0, 6],
    [5, 7],
    [3, 8],
    [5, 9],
    [6, 10],
    [8, 11],
    [8, 12],
    [2, 13],
    [12, 14],
]
outbound = 2e31 -1
# %%
schedules = sorted(schedules, key=lambda x: (x[1],x[0]))
# %%

meets = []
meets.append(schedules[0])
k = 0
for i in range(1, n):
    if schedules[i][1] <= 0 or schedules[i][0] > 2**31-1:
        continue
    # 이전 회의 끝나는 시간 <= 이후 회의 시작하는 시간 이여야 겹치지 않는다.
    if  schedules[k][1] <= schedules[i][0]:
        meets.append(schedules[i])
        k = i
print(meets)
# %%
