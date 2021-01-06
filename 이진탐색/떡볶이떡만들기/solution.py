#%%
n, m = 4, 6
array = [19,15, 10, 17]

# %%

start  = 0
end =  max(array)

while start <= end:
    mid = (start + end)//2
    length = 0
    for h in array:
        if h >= mid:
            length += (h - mid)

    if length == m:
        print(mid)
        break
    elif length > m:
        start = mid+1
    else:
        end = mid -1



# %%
