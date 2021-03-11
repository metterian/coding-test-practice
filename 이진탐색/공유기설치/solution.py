#%%
n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
# %%
array.sort()
# %%

left, right = 1, array[-1] - array[0]
result = 0
while left <= right:
    mid = left+(right-left)//2


    value = array[0]
    count = 1
    for i in range(1, n):
        if value + mid <= array[i]:
            count += 1
            value = array[i]

    if count >= c:
        result = mid
        left = mid + 1
    else:
        right = mid -1

print(result)



# %%
