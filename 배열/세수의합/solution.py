# %% [markdown]
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리면트를 출력 해라
# <br>
# Input:
# <br>
# ```nums = [-1,0,1,2,-1,-4]  ```
#
# Output:
# ```[
#   [-1,-1,2],
#   [-1,0,1]
# ]```
# %%
nums = [-1,0,1,2,-1,-4]
# %%
from typing import *
# 브루트 포스로 계산
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j> i+1 and  nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k> j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    print(i,j,k)
                    result.append([nums[i], nums[j], nums[k]])
    return result
threeSum(nums)
# %%
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif three_sum > 0:
                right -= 1
            else:
                left += 1
    return result
threeSum(nums)

# %%
