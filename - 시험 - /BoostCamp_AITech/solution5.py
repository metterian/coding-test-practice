
#%%
from collections import Counter
n = 9
k = bin(n)
k = Counter(k[2:])['1']

answer = 0
for i in range(9):
    if k == Counter(bin(i)[2:])['1']:
        answer+=1
print(answer)

# %%
