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



# %%
binary_search([1,2,4], 2, 0, 2)
# %%
def binary_search(A, target, start, end):
    mid = (end - start)//2
    if A[mid] == target:
        return target
    elif target < A[mid]:
        binary_search(A, target, start, mid-1)

    else:
        binary_search(A, target, mid+1, end)
# %%
