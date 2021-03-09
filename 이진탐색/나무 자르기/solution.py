#%%
import sys
n, m = 4, 7
trees = list(sorted(map(int, '20 15 10 17'.split())))

# %%

def binary_search(arr, target, left, right):
    height = 0
    while left<=right:
        mid = left + (right-left)//2
        bundle = sum(map(lambda x: x-mid if x>=mid else 0, arr))
        if bundle <target:
            right = mid-1
        else:
            height = mid
            left = mid+1

    return height
binary_search(trees, m, 1, max(trees))

# %%

# %%
