#%%
import math
S = 200
left, right = 1,S

# %%
answer = 0
while left <= right:
    mid = left + (right-left)//2

    if mid*(mid+1)/2 <= S:
        answer = mid
        left = mid +1
    else:
        right = mid -1

print(answer)
# %%
