#%%
n, x = 7,2
A = [1,1,2,2,2,2,3]
start, end = 0, n-1

#%%
solution = 0
def search(A, target, start, end):
    global solution
    if start > end:
        return None
    mid = (end - start)//2
    if A[mid] == target and A[start] == target:
        return start

    elif target < A[mid]:
        search(A, target, start, mid-1)
    else:
        search(A, target, mid+1, end)
    return None





# %%
search(A, x, start, end)
print(solution)
# %%
