#%%
height = [0,1,0,2,1,0,1,3,2,1,2,1]


# %% [markdown]
## Two Point
#%%
from typing import *
def trap(height: List[int]) -> int:
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
#test
    volume = 0
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            volume += (left_max - height[left])
            left += 1
        else:
            volume += (right_max - height[right])
            right -= 1
    return volume

trap(height)

# %% [markdown]
## STACK
# %%
def trap(height: List[int]) -> int:
