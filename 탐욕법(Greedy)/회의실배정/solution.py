#%%
schedules = [
[4, 4],
[4, 4],
[3, 4],
[2, 4],
[1, 4],
]
def solution(schedules):
    schedules.sort(key=lambda x: (x[1], x[0]))
    start = schedules[0]


    start_answer = start
    answer = []
    for i in range(1, len(schedules)):
        if schedules[i][1] <= 0 or schedules[i][0] > 2**31-1:
            continue
        if start[1] <= schedules[i][0]:
            answer.append(schedules[i])
            start = schedules[i]

    return len([start_answer] + answer)

print(solution(schedules))
# %%

# %%
