#%%
n, target = 4,6
heights = [19,15, 10, 17]

# %%
def get_cutted_length(mid):
    return sum([h - mid for h in heights if h-mid > 0])
# %%


start = 0
end = max(heights)

while start <= end:
    mid = (start + end)//2
    print(get_cutted_length(mid), start, mid, end)
    if get_cutted_length(mid) < target:
        end = mid-1
    else:
        result = mid
        start = mid +1
print(result)
# %%
