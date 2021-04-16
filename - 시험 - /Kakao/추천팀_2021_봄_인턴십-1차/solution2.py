#%%
from math import *
cnt = 0
def function(n):
    global cnt
    if (n<3):
        cnt+=1
        return 1
    else:
        cnt+=1
        return function(ceil(sqrt(n)))

function(200)
# %%
print(cnt)
# %%
