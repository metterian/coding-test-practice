#%%
n = int(input())

# %%
value = 0
A = '12111'

from collections import Counter
A = A.split('0')
for a in A:
    n = len(a)
    consec = 1
    for i in range(1, n):
        if a[i-1] == a[i]:
            consec += 1
        else:
            consec = 1




# %%
