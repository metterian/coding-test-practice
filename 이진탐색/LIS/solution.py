#%%
n = 6
A = list(map(int, '10 20 10 30 20 50'.split()))
# %%
def binarySearch(arr, target):
    left, right = 1, len(arr)-1
    while left <= right:
        mid = left + (right-left)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid -1
        else:
            left = mid + 1
    return right



stack = [0]
for a in A:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[binarySearch(stack, a)] = a

print(len(stack)-1)
# %%
# Use Bisect Module
from bisect import bisect_left

stack = [0]
for a in A:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[bisect_left(stack,a)] = a

print(len(stack)-1)

# %%
