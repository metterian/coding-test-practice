#%%
n = 3
k = 4

# %%
left, right = 1, k

while left <= right:
    mid = left + (right-left)//2

    ordinal = 0
    for i in range(1, n+1):
        ordinal += min(n, mid//i)

    if ordinal >= k: #이분 탐색 실행
        answer = mid
        right = mid-1
    else:
        left = mid+1

print(answer)



# %%
