#%%
k, need = 1,1
lines = sorted([int(input()) for _ in range(k)])

# %%
def solution(lines, need):
    left, right = 1, max(lines)
    result = 0
    while left <= right:
        mid = left + (right-left)//2
        bundle = sum([line//mid for line in lines if line])
        if bundle < need:
            right = mid -1
        else:
            result = mid
            left  = mid + 1

    return (result)

solution(lines, need)

# %%
