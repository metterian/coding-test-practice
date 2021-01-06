#%%
N = 5
n = [8,3,7,9,2]
M = 3
m = [5,7,9]
n = sorted(n)
# %%
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return target
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# %%
for i in m:
    if binary_search(n, i, 0, N-1) != None:
        print("yes")
    else:
        print("no")
# %%
