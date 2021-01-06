#%%
n = list(map(int, list('123402')))

# %%
left, right = n[:len(n)//2], n[len(n)//2:]
if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
# %%
