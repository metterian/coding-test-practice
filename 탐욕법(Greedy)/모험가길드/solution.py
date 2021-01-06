#%%
n = 5
p = [2,3,1,2,2]

# %%
p = sorted(p, reverse=True)
i = 0
h = 0
while p[i:]:
    if p[i] >= p[-1] and p[i]>h:
        h+=p.pop()
    else:
        i+=1
        h=0

print(len(p))

# %%
