#%%
n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
# %%
array.sort()
# %%

left, right = array[1] - array[0], array[-1] - array[0]
result = 0
while left <= right:
    mid = (left+right)//2


    value = array[0]
    count = 1
    for i in range(1, n):
        if value + mid <= array[i]:
            count += 1
            value = array[i]

    if count < c:
        right = mid -1
    else:
        result = mid
        left = mid + 1

print(result)



# %%
