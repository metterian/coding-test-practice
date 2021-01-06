#%%
n = 5
a = [-15, -6, 1,3,7]
fixed = list(range(n))
# %%
def solution(array, start, end):
    if start > end:
        return None
    
    mid = (start + end )//2


    if array[mid] == mid:
        return mid
    elif  array[mid] < mid:
        return solution(array, mid+1, end)
    else:
        return solution(array, start, mid-1)

solution([-15, -4, 2,8,9, 13,15], 7, 6)
# %%
