#%%
def binary_search(array, target, start, end):
    while start<= end:
        mid = (start + end)//2
        if array[mid] == target:
            return target
        elif target < array[mid]:
            end = mid -1
        else:
            start = mid + 1
    return None

#%%
n = 7
count = 0
def solution(array, target, start, end):
    global count

    if start > end:
        return None

    mid = (start+end)//2
    if array[mid] == target:
        count+=1
    solution(array, target, start, mid-1 )
    solution(array, target, mid+1, end)


solution([1,1,2,2,2,2,3], 4, 0, n-1)
if count:
    print(count)
else:
    print(-1)

# %%
