#%%
n = 3
k = 7

# %%
left, right = 1, k
answer = 0
while left <= right:
    mid = left + (right-left)//2

    ordinal = 0
    for i in range(1, n+1):
        ordinal += min(n, mid//i)

    if ordinal >= k:
        answer = mid
        right = mid-1
    else:
        left = mid+1

print(answer)


# %%
