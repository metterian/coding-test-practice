#%%

nums = [4,1,2,3,1,0,5]
#%%
from collections import deque
def solution(nums):
    visited = [False] * len(nums)
    def bfs(nums, start, visited):
        queue = deque([[start, 0]])
        visited[start] = True

        while queue:
            now, times = queue.popleft()
            if not nums[now]:
                continue
            if now == len(nums) - 1:
                return times
            forward, backward = now + nums[now], now - nums[now]
            if 0< forward < len(nums) and not visited[forward]:
                visited[forward] = True
                queue.append([forward, times+1])
            if 0< backward < len(nums) and not visited[backward]:
                visited[backward] = True
                queue.append([backward, times+1])
    return bfs(nums, 0, visited)
print(solution(nums))
# %%
