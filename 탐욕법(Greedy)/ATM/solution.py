#%%
n = int(input())
p = list(map(int, input().split()))

# %%
p.sort()
time = p[0]
for i in range(1,n):
    p[i] += time
    time = p[i]

print(sum(p))
# %%
