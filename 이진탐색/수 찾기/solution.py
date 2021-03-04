#%%

N = 5
A = list(map(int, '4 1 5 2 3'.split()))
M= 5
targets = list(map(int, '1 3 7 9 5'.split()))
A.sort()

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2;
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return False

for target in targets:
    if binarySearch(A, 0, N-1, target):
        print(1)
    else:
        print(0)

# %%
