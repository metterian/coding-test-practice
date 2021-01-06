#%%
n,m = 5,3
W = [1,3,2,3,2]
W = [0] +W

# %%
answer = []

for i in range(1,n+1):
    for j in range(i+1, n+1):
        if W[i] !=W[j] and (i, j) not in answer:
            answer.append((i,j))

print(len(answer))
# %%
