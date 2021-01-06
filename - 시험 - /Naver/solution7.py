#%%

nums = [4,1,2,3,1,0,5]
#%%
import sys
min_jumps = sys.maxsize
def solution(nums):


    def jump(i, jumps):
        global min_jumps
        if i<0 or not nums[i] or  i > len(nums) or min_jumps > jumps:
            return
        if nums[i] == nums[-1]:
            min_jumps = min(min_jumps, jumps)
            return
        else:
            jump(i + nums[i], jumps +1)
            jump(i -nums[i], jumps +1)



    jump(0, 0)
    return min_jumps

print(solution(nums))
# %%
