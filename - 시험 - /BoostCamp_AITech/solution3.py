#%%
from itertools import chain
n = 5
s = list(range(1,n+1))
seqeunce = [1,2,3,4,5]



#%%
def find_reverse(s, start, end):
    dist = 0

    for i in s[::-1]:

        if i == end:
            dist+=1
            break
        else:
            dist+=1
    return dist

find_reverse(s, 4,3)





#%%
seq = []
for i in range(len(seqeunce)-1):
    seq.append((seqeunce[i], seqeunce[i+1]))

dist = 0
if n%2 ==0:
    pass


else:
    start, end = min(s), max(s)
    mid = n//2
    for start, end in seq:
        dist += min(find_reverse(s, start, end), abs(end-start))
print(dist)
# %%
