#%%
n = 7
array = [15, 11,4,8,5,2,4]
# %%
count = []
for i in range(1, len(array)):
    if array[i-1] < array[i]:
        count.append(i)


print(count)
# %%
