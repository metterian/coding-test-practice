#%%
from collections import deque, Counter
from math import ceil

progresses = deque([95, 90, 99, 99, 80, 99])
speeds = deque([1, 1, 1, 1, 1, 1])
# %%
workings = []

def soultion(progresses, speeds):
    de_day = []
    left_day = float('-inf')
    for p, s in zip(progresses, speeds):
        if left_day >= ceil((100 - p)/s):
            de_day.append(left_day)
        else:
            left_day = ceil((100 - p)/s)
            de_day.append(left_day)
    answer = Counter(de_day).values()
    return answer


# %%
print(soultion(progresses, speeds))
# %%
