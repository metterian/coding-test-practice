#%%
from typing import Tuple


nums = '0000'
answer = int(nums[0])
# %%

nums  = list(map(int, list(nums)))
nums = sorted(nums, reverse=True)
# %%
for i in nums:
    if i != 0:
        answer*= i
    else:
        answer += i



print(answer)

# %%

# %%
