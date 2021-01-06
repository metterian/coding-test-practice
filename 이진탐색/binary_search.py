#%%
def binary_search(A, target, start, end):
    while start <= end:
        mid  = (end - start)//2
        if A[mid] == target:
            return A[mid]
        elif target < A[mid]:
            end = mid -1
        else:
            start = mid +1
    return None




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
